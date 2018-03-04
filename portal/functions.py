import urllib.request
import json


def get_btcprice():
    with urllib.request.urlopen("https://www.bitstamp.net/api/ticker/") as url:
        data = json.load(url)
        price = round(float(data['last']), 8)
    return price
