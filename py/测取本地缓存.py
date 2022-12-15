#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : 测取本地缓存.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2022/9/19

import requests

r = requests.get('http://192.168.10.99:5705/txt/js/tg/Nike影视.js')
print(r)
print(r.text)