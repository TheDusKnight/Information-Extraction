import scrapy
import bs4 as bs
import os
import sys


class Birth(scrapy.Spider):
    name = 'birth'
    allowed_domains = ['www.imdb.com']

    start_urls = [
        'https://www.imdb.com/search/name/?birth_monthday=08-01&count=100',
    ]

    custom_settings = {
        'LOG_LEVEL': 'INFO',
    }

    def __init__(self):
        pass

    def parse(self, response):
        self.logger.info('Index page ' + response.url)
        next_page = response.css("div.desc a.lister-page-next.next-page::attr(href)").get()
        content_pages = response.css("div.lister-item.mode-detail h3.lister-item-header a::attr(href)").getall()

        if next_page != "/search/name/?birth_monthday=08-01&count=100&start=301":
            yield response.follow(next_page, callback=self.parse)
        else:
            self.logger.info("Reached 500 page " + next_page)

        for page in content_pages:
            yield response.follow(page + "/bio?ref_=nm_ov_bio_sm", callback=self.parse_page1)

        return

    def parse_page1(self, response):
        scrape_count = self.crawler.stats.get_value('item_scraped_count')
        self.logger.info("Content page " + response.url)
        self.logger.info(scrape_count)

        # if scrape_count == 499:
        #     self.crawler.engine.close_spider(self, "Closing spider")

        url = response.url
        bio = response.css("div.soda.odd p").get()

        if bio:
            bio = bs.BeautifulSoup(bio, features="lxml").getText().strip()
            if bio and bio.lower() != "tbd" and bio.lower() != "tba":
                yield {
                    "url": url,
                    "bio": bio,
                }
        else:
            self.logger.info("bio not found")

        return
