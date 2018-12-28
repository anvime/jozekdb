import json
import dbModel
import app
from pprint import pprint
from collections import namedtuple

class Product(object):
    def __init__(self, name, currentPrice, originalPrice):
        self.name = name
        self.originalPrice = originalPrice
        self.currentPrice = currentPrice

def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Product':
        return Product(obj['name'], obj['originalPrice'], obj['currentPrice'])
    return obj


with open('miler.json') as data_file:
    data = json.load(data_file)
# pprint(data)

for x in data:
    newProduct = dbModel.Product(name=x['name'], originalPrice=x['originalPrice'], currentPrice=x['currentPrice'])
    app.db.session.add(newProduct)
    app.db.session.commit()

#TODO rzutowanie na obiekt, potem zapisywanie do bazy danych