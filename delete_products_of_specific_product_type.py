import requests
import json
from math import ceil
from time import sleep
from configparser import ConfigParser

TYPE_OF_PRODUCTS_TO_DELETE = 'Photo'

config_parser = ConfigParser()
config_parser.read('.credentials')

api_key = config_parser['default']['API_KEY']
password = config_parser['default']['PASSWORD']
store_url_prefix = config_parser['default']['STORE_URL_PREFIX']

url_prefix = 'https://%s:%s@%s.myshopify.com/admin/' % (api_key, password, store_url_prefix)

count_url = url_prefix + 'products/count.json'

session = requests.Session()

session.headers.update({'Content-Type': 'application/json'})

parameters = {
        'product_type': TYPE_OF_PRODUCTS_TO_DELETE
    }

response = session.get(count_url, params=parameters)

if response.status_code != 200:
    raise Exception('Status code: [%d] Unable to get URL: [%s]' % (response.status_code, count_url))

sleep(0.5)

number_of_products = json.loads(response.text)['count']

num_pages = ceil(number_of_products / 250)

for i in range(num_pages):
    products_url = url_prefix + 'products.json'

    parameters = {
        'limit': 250,
        'fields': 'id',
        'product_type': TYPE_OF_PRODUCTS_TO_DELETE
    }

    response = session.get(products_url, params=parameters)

    if response.status_code != 200:
        raise Exception('Status code: [%d] Unable to get with URL: [%s]' % (response.status_code, products_url))

    sleep(0.5)

    products = json.loads(response.text)['products']

    for product in products:
        product_id = product['id']

        product_url = url_prefix + 'products/%d.json' % product_id

        response = session.delete(product_url)

        if response.status_code != 200:
            raise Exception('Status code: [%d] Unable to delete with URL: [%s]' % (response.status_code, product_url))

        sleep(0.5)
