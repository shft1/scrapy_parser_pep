import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org']

    def parse(self, response):
        pep_urls = response.css('#numerical-index tbody tr td:nth-child(2) a')
        pass
