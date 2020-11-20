#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="test_db", user = "test", password = "test", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")

cur = conn.cursor()

cur.execute("SELECT id, name from test_schema.test_table")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1], "\n"

print "Operation done successfully";
conn.close()