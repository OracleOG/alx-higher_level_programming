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


def filter_table(db):
    """filters the table for the letter 'N'
    """
    try:
        cur = db.cursor()

        cur.execute("""SELECT * FROM states
                     WHERE states.name LIKE 'N%' ORDER BY id ASC""")
        rows = cur.fetchall()

        for row in rows:
            print("({}, '{}')".format(row[0], row[1]))

    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        sys.exit(1)


def main():
    """Main function for this script"""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = connect_db(username, password, database)

    # Print out table in a formatted style
    filter_table(db)

    # Close all cursors
    cur = db.cursor()
    cur.close()
    # Close the database connection
    db.close()


if __name__ == "__main__":
    main()
