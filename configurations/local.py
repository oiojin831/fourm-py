# --*-- encoding: utf-8 -*-
import os

DEBUG = True

SANDBOX = os.path.abspath(os.path.join(os.path.dirname(
        os.path.dirname(__file__)), 'sandbox'
))

if not os.path.exists(SANDBOX):
    os.makedirs(SANDBOX)

DATABASE = 'sqlite:///' + os.path.join(SANDBOX, 'db.db')

del os