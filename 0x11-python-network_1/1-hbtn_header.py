#!/usr/bin/python3
""" sends a request to the URL and displays the value of the header """
from urllib.request import Request, urlopen
import sys


if __name__ == "__main__":
    req = sys.argv[1]
    with urlopen(req) as response:
        html = response.info()

    print(html['X-Request-Id'])
