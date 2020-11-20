#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="test_db", user = "test", password = "test", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")
