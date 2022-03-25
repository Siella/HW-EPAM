import os

import pytest
from asynctest import CoroutineMock, patch

from homework10.converter import Converter
from homework10.my_parser import CompanyData, DataParser


def find_test_file(name):
    return os.path.join(
        os.path.dirname(__file__), name
    )


@patch("aiohttp.ClientSession.get")
@pytest.mark.asyncio
async def test_parser(mock_get):
    parser = DataParser(find_test_file('test_html.html'))
    company_dict = parser.parse_html_data()

    assert company_dict == {'3M': {'HRef': '/stocks/mmm-stock',
                                   'LatestPricePreviousClose':
                                       '177.00 176.77',
                                   '3Mo.+/-%':
                                       '0.23 0.13%'}}

    company = CompanyData('3M', company_dict['3M'])
    assert company.url == 'https://markets.businessinsider.com' \
                          '/stocks/mmm-stock'
    assert company.growth is None
    assert company.price_usd == 177.00

    mock_get.return_value.__aenter__.return_value.text = CoroutineMock(
        side_effect=[
            '<span class="price-section__category">'
            'Stock <span>, MMM</span></span>']
    )
    await company.get_data_from_href()
    assert company.code == 'MMM'


@patch("requests.Session.get")
def test_converter(mock_get):
    class FakeResponse:
        def __init__(self, **kwargs):
            self.__dict__ = kwargs

    test_response = FakeResponse(**{
        'text':
            '<Valute ID="R01235">'
            '<NumCode>840</NumCode>'
            '<CharCode>USD</CharCode>'
            '<Nominal>1</Nominal>'
            '<Name>Доллар США</Name>'
            '<Value>74,2926</Value>'
            '</Valute>',
        'content': 'some content',
        'status_code': 200,
        'encoding': 'ISO-8859-1',
        'reason': 'OK',
        'elapsed': 'OK'
    })
    mock_get.return_value = test_response
    conv = Converter()
    assert round(conv.usd_to_rubles(10), 3) == 742.926
