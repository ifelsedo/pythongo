#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Filename: httprequest.py

import urllib.request

r = urllib.request.Request('https://www.baidu.com')
try:
    response = urllib.request.urlopen(r)
    page = response.read()
    print(page)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read().decode("utf8"))

