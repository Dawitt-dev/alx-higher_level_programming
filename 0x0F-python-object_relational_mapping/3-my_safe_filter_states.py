#!/usr/bin/python3
"""
    A script that takes in an argument and displays all values.
"""
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
    argument = """ SELECT * FROM states\
                WHERE name = %s
                ORDER BY id ASC"""
    cur.execute(argument, (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
