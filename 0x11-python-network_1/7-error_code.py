#!/usr/bin/python3
"""
Task 7-Send a GET request to the passed URL and display the body of the
response,printing an error message for HTTP status codes >= 400
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    reqst = requests.get(argv[1])
    if reqst.status_code < 400:
        print(reqst.text)
    else:
        print('Error code: {}'.format(reqst.status_code))
