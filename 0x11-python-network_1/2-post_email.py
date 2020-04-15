#!/usr/bin/python3
"""
Task 2 - Send a POST request to the passed URL with email as a parameter and
display the body of the response
"""

if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    from sys import argv

    url = argv[1]
    values = {'email': argv[2]}

    dato = urllib.parse.urlencode(values)
    dato = dato.encode('ascii')
    request = urllib.request.Request(url, dato)
    with urllib.request.urlopen(request) as response:
        body = response.read()
    print(body.decode('utf-8'))
