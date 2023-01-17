import requests;
import config;
import random;
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
class StockAPIHandler():
    def __init__(self):
        self.url = config.BASE_URL
    def get_stock_price(self, symbol)        :
        try:
            data= {config.SYMBOL: symbol}
            url2 = self.url +"/realtime/stock/price"
            response = requests.post(url2, json=data,  verify=False)
            logger.debug("response")
            logger.debug(response.json()[config.CURRENT_STOCK_PRICE])
            return response.json()[config.CURRENT_STOCK_PRICE]
        except:
            logger.debug("in except")
            return random.randrange(100,900);