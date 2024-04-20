#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response"""
from urllib import parse, request
import sys


url = sys.argv[1]
values = {'email': sys.argv[2]}
data = parse.urlencode(values)
data = data.encode('ascii')
req = request.Request(url, data)
with request.urlopen(req) as response:
    html = response.read()
    print(html.decode('utf-8'))
