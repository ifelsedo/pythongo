#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Filename: mysql.py

import pymysql

# conn = pymysql.connect('localhost', 'root', '123', 'quliuliang');
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123',
                       db='quliuliang')
cur = conn.cursor()
cur.execute('SELECT * FROM jd_user WHERE userid = 16151')
data = cur.fetchone()
print(data)
conn.close()