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
