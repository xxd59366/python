import os
import scrapy

class DmozSpider(scrapy.Spider):
    name = "cangku"
    allowed_domains = ["cangku.icu"]
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53 ' 'AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/56.0.2924.87 Safari/537.36',
    'cookie': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IkVhMkxuNnBPSjNjWkJVTXgzbTZZa2c9PSIsInZhbHVlIjoiMUlpY1NnREYyXC9hR1F1RnYwV0FnUEl5ZFdlejI2TkVGMHVvN3k2WWFNdUZcL1wvM2ZDWGRVNUh4N2o2OTNlanh0WFhPMWZMSHRCMGtjSjdRNHZwZTMwWVRncGhSQitKOFFPZVZCdnU4WEJXMU41XC9OcHlVaW9IUkVUR1hyZlJmY0xGWEVjSGJ1RHczZ3V4d3JDU21Va2xqNGpYcXRyQWxyc2NIQWZRenlDOFRwdkdSV1RtdDB5ZWt2bDlydnh6dlNkMSIsIm1hYyI6IjcxOWY1NzA2ZDE2YjExZjQ2MmJlYzU2ZDI0OTliYTAwOTJiZmFjMzRiNTFjMzc0NDMyYjUyZWFmNTE4ZjRlM2YifQ==; _pk_id.5.5493=57d8880b52d5b0b8.1648529513.; _gid=GA1.2.501197170.1653073903; _pk_ses.5.5493=1; _ga=GA1.2.2026985960.1644371742; _ga_PQTTGRGE2D=GS1.1.1653457206.57.1.1653457402.0; XSRF-TOKEN=eyJpdiI6IkVmUkNwWWNcLytxVGhJU2UrTit5MkRBPT0iLCJ2YWx1ZSI6IjBHVERXNG41MkRGbUNKQVJzdFJJNndlQWhDMk5uQzVDM0NuTjB6aVhFQktvSzhTZ055Wkd6STI0Z25KSFBWc00iLCJtYWMiOiIwNzc1ZjY0NTkyNjJjYTg1ZTg2YzRjMWYxZWQwY2UyYzlhZTYzYWI0MDFhZjM2ODhkZTI5NmM0MjM2NDU5OTJiIn0=; cangku_laravel_session=eyJpdiI6InNcL05VNGF3b1QyTDcya29za0Vwc0NRPT0iLCJ2YWx1ZSI6Ijk2czVESGtLNW5CRTk5d1F0MHJ6T0VUXC9Fd1hkSTRcL1JoZFgxUDJsd0JiZ3V5ZnlPQUJHMjFZTVFIbk04TDhQayIsIm1hYyI6ImJmNjAwNDdlNzZiYzQzYWM5NTI5NTg3MDE4OTI5MDkzY2FiMTYzMGY0YzRmMmFhYjc0YTA4OGZiOGFmODUyMDYifQ=='
    }
    start_urls = [
        "https://cangku.icu"
    ]

    def start_requests(self):
        url = "https://weibo.com/u/{}".format(self.weibo_id)
        yield Request(url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        data = response.text
        for sel in response.xpath('//div'):
            print(sel)