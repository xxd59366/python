import scrapy

class DmozSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["cangku.icu"]
    start_urls = [
        "https://cangku.icu"
    ]

    def parse(self, response):
        for sel in response.xpath('//div'):
            print(sel)