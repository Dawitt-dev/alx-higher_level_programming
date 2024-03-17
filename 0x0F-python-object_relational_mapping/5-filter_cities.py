#!/usr/bin/python3
"""A script that lists states with a name starting with N from database"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    argument = """
                SELECT cities.name
                FROM states
                INNER JOIN cities ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """
    cur.execute(argument, (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join([city[0] for city in query_rows]))
    cur.close()
    db.close()
