#!/usr/bin/python3
""" Task 5-fetch the value of the X-Request-ID variable found in the header"""

if __name__ == '__main__':
    import requests
    from sys import argv
    reqst = requests.get(argv[1])
    print(reqst.headers.get('X-Request-ID'))
