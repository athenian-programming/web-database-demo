#!/usr/bin/env python3

# Based on https://www.postgresqltutorial.com/postgresql-python/connect/
# Data loaded by https://github.com/pambrose/database-demo

import psycopg2

from database_config import config
from student import Student


def fetch_all_students():
    conn = None
    try:
        params = config()
        print('Connecting to the Postgres database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('Running student query...')
        cur.execute('SELECT * FROM students')
        results = list()
        while True:
            row = cur.fetchone()
            if row is not None:
                results.append(Student(row[0], row[1], row[2], row[3], row[4], row[5]))
            else:
                break

        cur.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit(0)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    students = fetch_all_students()
    for student in students:
        print(student.email)
