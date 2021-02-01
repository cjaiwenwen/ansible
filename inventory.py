import requests
import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

result = {}
result['all'] = {}
result['all']['devices'] = []
def main(url):
    resp = requests.get(url).json()
    devices = resp['devices']
    for item in devices:
        result['all']['devices'].append(item)
    print(result)


if __name__ == '__main__':
    main('http://localhost:8000/api/v1/net_dev')

