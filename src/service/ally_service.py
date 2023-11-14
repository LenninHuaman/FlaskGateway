import urllib.request
import json

from src.model.ally_response import AllyResponse

def getAlly(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)[0]
    ally = AllyResponse(**dict)
    return ally