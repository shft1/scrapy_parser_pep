import scrapy

from pep_parse.constans import ENCODING, PEP_DASH
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_rows = response.css('#numerical-index tbody tr')
        for pep_row in pep_rows:
            url_pep = pep_row.css('td:nth-child(2) a::attr(href)').get()
            yield response.follow(
                url_pep,
                callback=self.parse_pep,
            )

    def parse_pep(self, response):
        response = response.replace(body=response.body.decode(ENCODING))
        num_name_list = response.css(
            'h1.page-title::text').get().split(PEP_DASH)
        number = int(num_name_list[0].split()[1])
        name = num_name_list[1]
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
