from requests import Session
import requests
import secrets
from pprint import pprint as pp

# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories'


class CMC:
    # https://coinmarketcap.com/api/documentation/v1/
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {
                        'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': token,
                        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/categories'
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def getPrice(self, symbol):
        url = self.apiurl + '/v2/cryptocurrency/quotes/latest'
        parameter = {'symbol': symbol}
        r = self.session.get(url, params=parameter)
        data = r.json()['data']
        return data

cmc = CMC(secrets.api)

pp(cmc.getPrice('BTC'))