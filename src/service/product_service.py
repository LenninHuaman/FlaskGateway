import urllib.request
import json

from src.model.product_response import ProductResponse

def getProduct(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)[0]
    product = ProductResponse(**dict)
    return product