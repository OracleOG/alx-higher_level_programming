#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -X OPTIONS "$1"
