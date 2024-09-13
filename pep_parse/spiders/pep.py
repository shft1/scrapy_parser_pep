import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org']

    def parse(self, response):
        pep_urls = response.css('#numerical-index tbody tr td:nth-child(2) a')
        for pep_url in pep_urls:
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        num_name_list = response.css('h1.page-title::text').get().split(' – ')
        number = int(num_name_list[0].split()[1])
        name = num_name_list[1]
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)

# дописал возврат items со спарсенными данными,
# но может в метод parse надо еще что-то добавить ;)
