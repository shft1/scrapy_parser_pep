import csv
import datetime as dt

from pep_parse.constans import BASE_DIR, DIALECT, ENCODING, FORMAT_DATE


class PepParsePipeline():
    def open_spider(self, spider):
        self.statuses = {'Статус': 'Количество'}

    def process_item(self, item, spider):
        status = item['status']
        self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        total_count = sum(list(self.statuses.values())[1:])
        self.statuses['Total'] = total_count
        results = list(self.statuses.items())
        time = dt.datetime.now().strftime(FORMAT_DATE)
        filename = f'status_summary_{time}.csv'
        filepath = BASE_DIR / 'results' / filename
        with open(filepath, 'w', encoding=ENCODING) as csv_file:
            writer_obj = csv.writer(csv_file, dialect=DIALECT)
            writer_obj.writerow(results[0])
            writer_obj.writerows(results[1:-1])
            writer_obj.writerow(results[-1])
