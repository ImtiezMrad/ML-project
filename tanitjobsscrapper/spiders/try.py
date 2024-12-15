from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "try"
    start_urls = [
        "https://www.keejob.com/offres-emploi/",
    ]

    def parse(self, response):
        filename = "try.html"
        Path(filename).write_bytes(response.body)