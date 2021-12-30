import asyncio
import json
import time
from collections import defaultdict

from homework10.converter import Converter
from homework10.my_parser import CompanyData, DataParser
from homework10.scraper import TableScraper

converter = Converter()

t1 = time.time()
scraper = TableScraper()
scraper.load_table_data()
t2 = time.time()
print(f"It took {t2 - t1} seconds")

parser = DataParser('table_scrapped.html')
company_data = parser.parse_html_data()
companies = [
    CompanyData(name, company_data[name]) for name in company_data
]

asyncio.set_event_loop(asyncio.new_event_loop())


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

data = defaultdict(dict)
for company in companies:
    data[company.name] = {
        'code': company.code,
        'price': converter.usd_to_rubles(company.price_usd),
        'P/E': company.pe_ratio,
        'growth': company.growth,
        'potential profit':
            converter.usd_to_rubles(company.potential_profit),
    }

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
