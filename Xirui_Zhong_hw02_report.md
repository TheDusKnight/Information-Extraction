# Task 1
The date I used is 08/01.

Commend to execute a crawler: `scrapy crawl birth -O Zhong_Xirui_hw02_bios.csv`.

# Task 2

## Task 2.1

Link: https://www.imdb.com/name/nm0005222/bio?ref_=nm_ov_bio_sm

Bio:

![image-20210202161615940](/Users/trevor/Google_Drive/Notes/_resources/image-20210202161615940.png)

## Task 2.2
`./source/birth_crawler/Xirui_Zhong_hw02_bios.csv Xirui_Zhong_hw02_cast0.jl 0`
`./source/birth_crawler/Xirui_Zhong_hw02_bios.csv Xirui_Zhong_hw02_cast1.jl 1`

## Task 2.3

### Lexical
- birthplace: precision = 1, recall = 0.556.
- education: precision = 0.917, recall = 0.917.
- parents: precision = 0.286, recall = 0.4.
- awards: precision = 0.583, recall = 0.5.
- performances: precision = 0.85, recall = 0.38.
- colleagues: precision = 0.222, recall = 0.301.

### Syntactic
- birthplace: precision = 1, recall = 0.556.
- education: precision = 1, recall = 1.
- parents: precision = 0.143, recall = 0.6
- awards: precision = 0.727, recall = 0.571.
- performances: precision = 0.85, recall = 0.38.
- colleagues: precision = 0.222, recall = 0.143.