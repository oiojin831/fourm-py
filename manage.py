# --*-- encoding: utf-8 -*-
""":mod:`manage` --- Project manager
~~~~~~~~~~~~~~~~~~~~~~~~~

Executable project manager

"""

import sys
import code
import importlib
import argparse

import sqlalchemy
from flask import g

import fourm.models as m
from fourm import app as application
from fourm.models import db

# import local module for configurations
sys.path.append('configurations')
local_config = importlib.import_module('local')

_configurations = {
    'local': local_config
}

# env variable will be configuration environment such as local, production
def make_app(env):
    return application.create_app(_configurations[env])


def shell(args):
    app = make_app(args.env)

    session = db.session
    local = dict(app=app,
                 models=m,
                 session=session,
                 g=g,
                 db=db,
                 s=sqlalchemy)

    with app.app_context():
        code.interact(local=local)


def runserver(args):
    app = make_app(args.env)

    host = args.host
    port = args.port

    debug = app.config.get('DEBUG', False)

    app.run(host=host, port=port, debug=debug)


def init(args):
    app = make_app(args.env)

    with app.app_context():
        m.create_tables()

def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser('Manager')
    parser.add_argument('-e', '--env', dest='env', metavar='ENV',
                        choices=['local'], default='local')

    subparsers = parser.add_subparsers()

    # Shell
    parser_shell = subparsers.add_parser('runserver')
    parser_shell.set_defaults(func=shell)

    # Run  server
    parser_runserver = subparsers.add_parser('runserver')
    parser_runserver.set_defaults(func=runserver)
    parser_runserver.add_argument('-t', '--host', dest='host', metavar='HOST',
                                  default='0.0.0.0')
    parser_runserver.add_argument('-p', '--port', dest='port', metavar='PORT',
                                  type=int, default=3000)

    # Create tables
    parser_init = subparsers.add_parser('init')
    parser_init.set_defaults(func=init)

    args = parser.parse_args(argv)
    args.func(args)

if __name__ == '__main__':
    main()