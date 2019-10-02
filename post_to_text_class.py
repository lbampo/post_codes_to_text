import requests
import json

def get_post_json(p_code):
    req_post = requests.get(f'https://postcodes.io/postcodes/{p_code}')
    req_json = req_post.json()

    return req_json

def open_read_file(file, post_item):
    try:
        opened_file = open(file, 'a')
        opened_file.write(post_item)

    except FileNotFoundError:
        print("File not found")

        