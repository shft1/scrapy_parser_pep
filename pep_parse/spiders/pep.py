import scrapy

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
                cb_kwargs={'row': pep_row}
            )

    def parse_pep(self, response, row):
        number = int(row.css('td:nth-child(2) a::text').get())
        name = row.css('td:nth-child(3) a::text').get()
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
