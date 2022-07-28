import requests
from config import consumer_key

stock = 'GOOG'
endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(stock)

payload = {
                'apikey': consumer_key,
                'periodType': 'day',
                'frequencyType': 'minute',
                'frequency': '30',
                'period': '1',
                'endDate': None,
                'startDate': None,
                'needExtendedHoursData': 'false'
            }

content = requests.get(url = endpoint, params = payload)

data = content.json()
print(data)