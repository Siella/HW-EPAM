import time

import requests
from bs4 import BeautifulSoup


class MaxRetriesError(Exception):
    pass


class BadUrlError(Exception):
    pass


def retry(times=5):
    def retry_wrapper(f):
        def retry_times(self, *args, **kwargs):
            success = False
            while not success:
                try:
                    # предполагаем, что первый аргумент - суффикс основного url
                    url_param = '' if not args else f'?p={args[0]}'
                    request = self.s.get(''.join([self.url, url_param]))
                    soup = BeautifulSoup(request.text, features='html.parser')
                    success = True
                except requests.exceptions.Timeout:
                    wait = self.retries * 30
                    self.retries += 1
                    if self.retries > times:
                        raise MaxRetriesError(
                            'Cannot do a request (timeout error)'
                        )
                    time.sleep(wait)
                except requests.exceptions.TooManyRedirects:
                    raise BadUrlError(
                        'Cyclic redirects exceeded max request number!'
                    )
                except requests.exceptions.RequestException as e:
                    raise SystemExit(e)
            return f(self, soup, *args, **kwargs)
        return retry_times
    return retry_wrapper
