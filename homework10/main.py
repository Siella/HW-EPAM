import json
import time
from collections import defaultdict

from converter import Converter
from my_parser import CompanyData, DataParser
from scraper import TableScraper

converter = Converter()

scraper = TableScraper()
scraper.load_table_data()

parser = DataParser('table_scrapped.html')
company_data = parser.parse_html_data()
data = defaultdict(dict)

start_time = time.time()
for name in company_data:
    company = CompanyData(name, company_data[name])
    data[name] = {
        'code': company.code,
        'price': converter.usd_to_rubles(company.price_usd),
        'P/E': company.pe_ratio,
        'growth': company.growth,
        'potential profit':
            converter.usd_to_rubles(company.potential_profit),
    }
print("--- %s seconds ---" % (time.time() - start_time))
with open('all_companies_data.json', 'w') as json_file:
    json.dump(data, json_file)

# with open('all_companies_data.json') as json_file:
#     data = json.load(json_file)

top_10_high_price = dict(
    sorted(
        data.items(),
        key=lambda x: (x[1]["price"] is None, x[1]["price"]),
        reverse=True)[:10]
)
top_10_low_pe = dict(
    sorted(
        data.items(),
        key=lambda x: (x[1]["P/E"] is None, x[1]["P/E"]))[:10]
)
top_10_high_growth = dict(
    sorted(
        data.items(),
        key=lambda x: (x[1]["growth"] is None, x[1]["growth"]),
        reverse=True)[:10]
)
top_10_high_potential_profit = dict(
    sorted(
        data.items(),
        key=lambda x: (x[1]["potential profit"] is None,
                       x[1]["potential profit"]),
        reverse=True)[:10]
)

to_json = zip(
    [
        top_10_high_price,
        top_10_low_pe,
        top_10_high_growth,
        top_10_high_potential_profit,
    ],
    [
        'top_10_high_price',
        'top_10_low_pe',
        'top_10_high_growth',
        'top_10_high_potential_profit'
    ]
)
for dict_, name in to_json:
    with open(f"{name}.json", "w") as json_file:
        json.dump(dict_, json_file)
