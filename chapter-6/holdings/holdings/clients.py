import requests
import cachetools

class MarketDataClient(object):

    base_url = 'http://market-data:8000'

    def _make_request(self, url):
        response = requests.get(f"{self.base_url}/{url}", headers={'content-type': 'application/json'})
        return response.json()

    @retry(stop=stop_after_attempt(3),
           before=before_log(logger, logging.DEBUG))
    def all_prices(self):
        return self._make_request("prices")

    def price(self, code):
        return self._make_request(f"prices/{code}")
