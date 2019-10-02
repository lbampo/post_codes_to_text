import requests
import json

def get_post_json(p_code):
    req_post = requests.get(f'https://postcodes.io/postcodes/{p_code}')
    req_json = req_post.json()

    return req_json

