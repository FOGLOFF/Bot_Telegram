import os
import json
from dotenv import load_dotenv
from requests import request
from date_b import *

path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(path):
    load_dotenv(path)
    APP_ID = os.environ.get('APP_ID')


def latest():
    """Заполнение БД через АPI"""
    response = request(
        method='GET',
        url='https://api.opendota.com/api/heroes'
    )

    respon = response.json()

    if response.status_code == 200:
        for i in respon:
            print(i)
            inp(i['localized_name'], i['primary_attr'], i['attack_type'], i['legs'])

    else:
        print({})



