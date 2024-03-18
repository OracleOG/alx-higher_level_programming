#!/usr/bin/python3
"""
using the MySQLdb module
"""

import MySQLdb
import sys


def connect_db(username, password, database):
    """ Function that initiates connection to MySQLdb
    using provided arguments"""
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database
        )
        return db
    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)


def list_cities(db, param):
    """filters the table for rows containg the parameter 'xname'
    """
    try:
        cur = db.cursor()

        # Use parameterized query to prevent SQL injection
        query = """SELECT cities.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name like %s ORDER BY cities.id ASC"""

        cur.execute(query, (param + '%',))

        rows = cur.fetchall()

        x = len(rows)

        for row in rows:
            if x > 1:
                print("{}, ".format(row[0]), end='')
            else:
                print("{}".format(row[0]))
            x -= 1

    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        sys.exit(1)


def main():
    """Main function for this script
    the SQL commad is Free of SQL injections"""
    if len(sys.argv) != 5:
        print("""Usage: {} <username> <password> <database>/
               <name of citie>""".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    param = sys.argv[4]

    # Connect to the database
    db = connect_db(username, password, database)

    # Print out table in a formatted style
    list_cities(db, param)

    # Close all cursors
    cur = db.cursor()
    cur.close()
    # Close the database connection
    db.close()


if __name__ == "__main__":
    main()
