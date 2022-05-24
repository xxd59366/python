import scrapy

class DmozSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["cangku.icu"]
    start_urls = [
        "https://cangku.icu/api/v1/post/list?page=1&per_page=18&with[]=user&with[]=categories&include=user,categories:simple&simple=1"
    ]

    def parse(self, response):
        for sel in response.xpath('//div'):
            print(sel)