#!/usr/bin/python3
""" project on http request with python """
from urllib.request import Request, urlopen


req = Request('https://alx-intranet.hbtn.io/status')
with urlopen(req) as response:
    html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode("utf-8")))