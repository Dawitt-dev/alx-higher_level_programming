#!/usr/bin/python3
"""A script that lists states with a name starting with N from database"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name\
                FROM states s, cities c\
                WHERE c.state_id = s.id\
                ORDER BY c.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
