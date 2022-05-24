import scrapy

# class DmozSpider(scrapy.Spider):
#     name = "pixiv"
#     allowed_domains = ["pixiv.net"]
#     start_urls = [
#         "https://pixiv.net"
#     ]

class TestSpider(scrapy.Spider):
    name = 'pixiv'
    allowed_domains = ['pixiv.net']
    start_urls = [
        'https://pixiv.net'
    ]


    def parse(self, response):
        print("parse-->", response.text)
    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
    # def parse(self, response):
    #     for sel in response.xpath('//div'):
    #         print(sel)