# -*- endcoding: utf-8 -*-
"""
"""
import os
import tempfile
import collections

from flask import Flask

import resource
import blueprints
import models as m
from models import db
from util.ext.sqlalchemy_ext import engine_url

def create_app(config):
    app = Flask(__name__)
    if isinstance(config, collections.Mapping):
        app.config.update(config)
    else:
        app.config.from_object(config)

    # SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = engine_url(app.config['DATABASE'])
    db.init_app(app)

    # Blueprints
    blueprints.register_blueprints(app)

    return app