#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
 Usage: ./0-select_states.py <mysql username> \
                             <mysql password> \
                           <database name>
                           """

import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = database.cursor()
    c.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE states.name=%s", (sys.argv[4],))
    row = c.fetchall()
    tmp_list = []
    for data in row:
        tmp_list.append(data[0])
    print(*tmp_list, sep=", ")
    c.close()
    database.close()
