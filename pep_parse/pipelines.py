import csv
import datetime as dt

from pep_parse.constains import BASE_DIR, FORMAT_DATE


class PepParsePipeline():
    def open_spider(self, spider):
        self.count_pep = 0
        self.count_status = {}

    def process_item(self, item, spider):
        status = item['status']
        self.count_pep += 1
        self.count_status[status] = self.count_status.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        results = list(self.count_status.items())
        time = dt.datetime.now().strftime(FORMAT_DATE)
        filename = f'status_summary_{time}.csv'
        filepath = BASE_DIR / 'results' / filename
        with open(filepath, 'w', encoding='utf-8') as csv_file:
            writer_obj = csv.writer(csv_file, dialect='unix')
            writer_obj.writerow(['Статус', 'Количество'])
            writer_obj.writerows(results)
            writer_obj.writerow(['Total', str(self.count_pep)])
