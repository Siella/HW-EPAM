import re

import requests

from homework10.request_util import retry

URL = 'https://markets.businessinsider.com/index/components/s&p_500'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36'
}
MAX_RETRIES = 5


class TableScraper:
    """
    Class that scraps data of the main table
    from markets.businessinsider.com.

    :param url: MARKETS INSIDER web-site URL
    :type url: str
    :param s: requests session
    :type s: requests.Session
    :param page_nums: table's number of pages
    :type page_nums: int
    """
    def __init__(self):
        self.url = URL
        self.s = requests.Session()
        self.s.headers.update(HEADERS)
        self.page_nums = self.get_number_of_pages()

    @retry(times=MAX_RETRIES)
    def get_number_of_pages(self, soup) -> int:
        """Gets number of table's pages."""
        pattern = r'<a href="\?p=[0-9]+">(<strong>){0,1}' \
                  '[0-9]+(</strong>){0,1}</a>'
        page_list = [str(p) for p in
                     soup.find(
                         'div', {'class': 'finando_paging'}
                     ).find_all('a')
                     if re.match(pattern, str(p)) is not None]
        return int(re.search(r'\d+', page_list[-1]).group(0))

    @retry(times=MAX_RETRIES)
    def get_table_headers(self, soup):
        """Gets table's column names."""
        return soup.find('thead', {'class': 'table__thead'})

    @retry(times=MAX_RETRIES)
    def get_one_page_table_data(self, soup, page: int):
        """Scraps data from one table's page"""
        return soup.find('tbody', {'class': 'table__tbody'})

    def load_table_data(self, file_name='table_scrapped', encoding='utf-8'):
        """Scraps and load data from all table's pages into one html file."""
        with open(f'{file_name}.html', 'w', encoding=encoding) as f:
            f.write(str(self.get_table_headers()))
            for page in range(1, self.page_nums + 1):
                f.write(str(self.get_one_page_table_data(page)))


if __name__ == '__main__':
    scraper = TableScraper()
    scraper.load_table_data()
