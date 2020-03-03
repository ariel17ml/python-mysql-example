#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="mysql",
    auth_plugin='mysql_native_password'
)

db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE employee(\
                  id INT AUTO_INCREMENT PRIMARY KEY, \
                  name VARCHAR(255), salary INT(6))")
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
    print(table)
