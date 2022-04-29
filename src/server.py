#!/usr/bin/env python3


import argparse
import logging
import os

from flask import Flask
from flask import Response
from flask import abort
from flask import jsonify
from flask_httpauth import HTTPBasicAuth

from database_students import fetch_all_students
from utils import setup_logging

PORT = 'port'
LOG_LEVEL = 'loglevel'

logger = logging.getLogger(__name__)

auth = HTTPBasicAuth()
http = Flask(__name__)


@http.route('/')
def root():
    return Response('You have reached the Athenian web-database-demo', mimetype='text/plain')


@http.route('/students-json', methods=['GET'])
def students_json():
    students = fetch_all_students()
    if len(students) == 0:
        abort(404)
    s = map(lambda x: x.__dict__, students)
    return jsonify({'students': list(s)})


@http.route('/students-html', methods=['GET'])
def students_html():
    students = fetch_all_students()
    if len(students) == 0:
        abort(404)

    names = ''
    for student in students:
        names += f'<tr> <td> {student.email} </td> <td> {student.grad_year} </td> </tr>'

    text = f'''
    <html>
        <head>
        </head>
        <body>
            <table>
            {names}
            </table>
        </body>
    </html>
    '''
    return Response(text, mimetype='text/html')


def main():
    # Parse CLI args
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest=PORT, default=8080, help='HTTP port [8080]')
    parser.add_argument('-v', '--verbose', dest=LOG_LEVEL, default=logging.INFO, action='store_const',
                        const=logging.DEBUG, help='Enable debugging info')
    args = vars(parser.parse_args())

    # Setup logging
    setup_logging(level=args[LOG_LEVEL])

    port = int(os.environ.get('PORT', args[PORT]))
    logger.info(f"Starting server listening on port {port}")

    http.run(debug=False, port=port, host='0.0.0.0')


if __name__ == "__main__":
    main()
