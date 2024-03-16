#!/usr/bin/python3
"""A script that lists states with a name starting with N from database"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd="q1w2e3",
                         db=sys.argv[3]
                         )
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY  'N%'\
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
