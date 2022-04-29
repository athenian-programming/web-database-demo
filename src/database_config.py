#!/usr/bin/env python3

import os
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    db = {}

    host = os.environ.get('DB_HOST')
    name = os.environ.get('DB_NAME')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')

    if (host is not None) and (name is not None) and (user is not None) and (password is not None):
        db['host'] = host
        db['database'] = name
        db['user'] = user
        db['password'] = password
        return db

    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return db
