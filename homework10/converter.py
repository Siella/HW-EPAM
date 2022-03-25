import re

import requests

from homework10.request_util import retry

URL = 'https://www.cbr.ru/scripts/XML_daily.asp'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.77 Safari/537.36'
}
MAX_RETRIES = 5


class Converter:
    """
    Class that gets currencies (USD) from CBR web-site
    and converts it to rubles.

    :param url: CBR web-site URL
    :type url: str
    :param s: requests session
    :type s: requests.Session
    """
    def __init__(self):
        self.url = URL
        self.s = requests.Session()
        self.s.headers.update(HEADERS)
        self.get_usd_currency()

    @retry(times=MAX_RETRIES)
    def get_usd_currency(self, soup) -> float:
        usd_tag = soup.find(
            'charcode', text=re.compile('USD')
        ).parent
        self.usd_in_rubles = float(usd_tag.value.text.replace(',', '.'))

    def usd_to_rubles(self, usd_val: float = 0.0) -> float:
        try:
            return usd_val * self.usd_in_rubles
        except (ValueError, TypeError):
            return None


if __name__ == '__main__':
    conv = Converter()
    print(conv.usd_to_rubles(10))
