#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
 Usage: ./0-select_states.py <mysql username> \
                             <mysql password> \
                           <database name>\
                           <state name>
                           """
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    row = cur.fetchall()
    for data in row:
        print(data)
    cur.close()
    database.close()
