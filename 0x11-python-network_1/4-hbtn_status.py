#!/usr/bin/python3
""" Task 4-Fetch https://intranet.hbtn.io/status using the requests package"""

if __name__ == '__main__':
    import requests
    reqst = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}'.format(type(reqst.text)))
    print('\t- content: {}'.format(reqst.text))
