import scrapy
import uuid
from datetime import datetime
import bs4 as bs
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
        next_page = response.css("div.desc a::attr(href)").get()
        content_pages = response.css("div.lister-item.mode-detail h3.lister-item-header a::attr(href)").getall()

        if response.url == "https://www.imdb.com/search/name/?birth_monthday=08-01&count=100&start=101":
            self.crawler.engine.close_spider(self, "Reached 500 bios, closing crawler now.")

        for page in content_pages:
            # self.logger.info("Follow page " + page+"/bio?ref_=nm_ov_bio_sm")
            yield response.follow(page+"/bio?ref_=nm_ov_bio_sm", callback=self.parse_page1)

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        return

    def parse_page1(self, response):
        scrape_count = self.crawler.stats.get_value('item_scraped_count')
        self.logger.info("Content page " + response.url)
        self.logger.info(scrape_count)

        url = response.url
        bio = response.css("div.soda.odd p").get()

        if bio:
            bio = bs.BeautifulSoup(bio, features="lxml").getText().strip()
            if bio and bio.lower() != "tbd" and bio.lower() != "tba":
                yield {
                    "url": url,
                    "bio": bio,
                }

        return


    # def parse_page1(self, response):
    #     self.logger.info('Content page ' + response.url)
    #     uid = uuid.uuid1().hex
    #     self.logger.info("id " + uid)
    #
    #     name = response.css('h1.person_title::text').get()
    #     if not name:
    #         name = " "
    #     else:
    #         name = name.strip()
    #         if name.lower() == "tbd" or name.lower() == "tba":
    #             name = " "
    #
    #
    #     # 所有title, year, role集合
    #     titles = response.css('table.credits.person_credits td.title.brief_metascore a::text').getall()
    #     years = response.css('table.credits.person_credits td.year::text').getall()
    #     roles = response.css('table.credits.person_credits td.role::text').getall()
    #
    #     # limits to at most 5 movies
    #     limit = min(5, len(titles))  # if not titles, then for loop will not be executed
    #     movies = []
    #     for i in range(limit):
    #         cur_title = titles[i]
    #         cur_year = years[i]
    #         cur_role = roles[i]
    #
    #         if not cur_title:
    #             cur_title = " "
    #         else:
    #             cur_title = cur_title.strip()
    #             if cur_title.lower() == "tbd" or cur_title.lower() == "tba":
    #                 cur_title = " "
    #
    #         if not cur_year:
    #             cur_year = -1
    #         else:
    #             cur_year = cur_year.strip()
    #             if cur_year.lower() == "tbd" or cur_year.lower() == "tba":
    #                 cur_year = -1
    #             else:
    #                 try:
    #                     cur_year = datetime.strptime(cur_year, '%b %d, %Y').year
    #                 except ValueError:
    #                     self.logger.info("Date does not match pattern, set to -1")
    #                     cur_year = -1
    #
    #         if not cur_role:
    #             cur_role = " "
    #         else:
    #             cur_role = cur_role.strip()
    #             if cur_role.lower() == "tbd" or cur_role.lower() == "tba":
    #                 cur_role = " "
    #
    #         movies.append({"name": cur_title, "year": cur_year, "role": cur_role})
    #
    #     yield {
    #         "id": uid,
    #         "url": response.url,
    #         "timestamp_crawl": datetime.now(),
    #         "name": name,
    #         "movies": movies,
    #     }
    #
    #     return
