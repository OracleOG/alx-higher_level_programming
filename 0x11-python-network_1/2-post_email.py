#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
from urllib.request import urlopen, Request
from urllib import parse
import sys


url = sys.argv[1]
data = {'email': sys.argv[2]}
data = parse.urlencode(data)
req = Request(url)
with urlopen(url, data) as response:
    html = response.read()
