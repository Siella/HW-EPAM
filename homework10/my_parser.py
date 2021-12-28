import asyncio
import re
import time
from collections import defaultdict
from typing import Dict

import aiohttp
from bs4 import BeautifulSoup

URL = 'https://markets.businessinsider.com'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36'
}
MAX_RETRIES = 5


class DataParser:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_html_data(self):
        with open(self.file_name, 'r') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'lxml')
            return soup

    pattern_span = r'</*span[\w*\W*]*?>'
    pattern_td = r'</*td[\w*\W*]*?>'
    pattern_br = r'<br/>'
    pattern_hr = r'<ahref="|"title="[\w\W\d]*"?'

    def _parse_tag(self, tag):
        new_tag = re.sub(
            f'\\s|{self.pattern_span}|{self.pattern_td}',
            '', str(tag), count=100
        )
        new_tag = re.sub(f'{self.pattern_hr}', '', new_tag, count=100)
        return re.sub(f'{self.pattern_br}', ' ', new_tag, count=100)

    def parse_html_data(self):
        soup = self.read_html_data()
        headers = [re.sub('\\s', '', tag.text, count=20) for tag
                   in soup.thead.find_all('th')]
        headers[0] = 'HRef'
        data = [self._parse_tag(tag)
                for tbody in soup.find_all('tbody')
                for tag in tbody.find_all('td')]
        names = [tag.text for tbody in soup.find_all('tbody')
                 for tag in tbody.find_all('a')]
        company_data = defaultdict(dict)
        k = len(headers)
        for i, name in enumerate(names):
            company_data[name] = dict(zip(headers, data[i*k:i*k+k]))
        return company_data


class CompanyData:
    def __init__(self, name: str, data: Dict):
        self.name = name
        self._data = data
        self.get_data_from_dict()
        self.url = ''.join([URL, self._data['HRef']])

    def get_data_from_dict(self):
        try:
            self.price_usd = float(re.search(
                r'[0-9]*[.][0-9]*',
                self._data['LatestPricePreviousClose']
            ).group(0))
        except ValueError:
            self.price_usd = None
        try:
            _, self.growth = self._data['1Year+/-%'].split(' ')
            self.growth = float(self.growth[:-1])
        except ValueError:
            self.uptake, self.drop = None, None

    async def get_data_from_href(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                await asyncio.sleep(0.01)
                html = await response.text()
                soup = BeautifulSoup(html, features='html.parser')
                self.code = soup.find(
                    'span', {'class': 'price-section__category'}
                ).text.strip().split(' , ')[-1]

                def find_value_by_tag_text(text):
                    try:
                        return float(
                            re.search(
                                r'[0-9]*[.][0-9]*',
                                soup.find(
                                    'div', text=re.compile(text)
                                ).parent.text
                            ).group(0))
                    except (ValueError, AttributeError):
                        return None

                self.pe_ratio = find_value_by_tag_text("P/E Ratio")
                self.week_low = find_value_by_tag_text("52 Week Low")
                self.week_high = find_value_by_tag_text("52 Week High")

                try:
                    self.potential_profit = self.week_low - self.week_high
                except (ValueError, TypeError):
                    self.potential_profit = None


if __name__ == '__main__':
    parser = DataParser('table_scrapped.html')
    data = parser.parse_html_data()
    companies = [CompanyData(name, data[name]) for name in data]

    async def get_data():
        tasks = [
            asyncio.create_task(
                company.get_data_from_href()
            ) for company in companies
        ]

        t1 = time.time()
        await asyncio.gather(*tasks)
        t2 = time.time()

        print(f"It took {t2 - t1} seconds")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_data())
    loop.close()
    print(companies[-1].code, companies[-1].week_high)
