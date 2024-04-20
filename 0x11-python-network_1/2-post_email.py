#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
"""
from urllib.request import urlopen, Request
from urllib import parse
import sys


url = sys.argv[1]
values = {'email': sys.argv[2]}
data = parse.urlencode(values)
data = data.encode('ascii')
req = Request(url, data)
with urlopen(req) as response:
    html = response.read()
    print(html.decode('utf-8'))
