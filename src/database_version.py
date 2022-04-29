#!/usr/bin/env python3

# Based on https://www.postgresqltutorial.com/postgresql-python/connect/

import psycopg2

from database_config import config


def version():
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the Postgres server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute('SELECT version()')

        # display the Postgres database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the Postgres
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    version()
