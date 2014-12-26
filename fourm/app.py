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
from util.middlewares.scssmiddleware import ScssMiddleware

def create_app(config):
    app = Flask(__name__)

    # Secret key for session //todo need to move somewhere
    app.secret_key = "hahah ahahah0"

    if isinstance(config, collections.Mapping):
        app.config.update(config)
    else:
        app.config.from_object(config)

    # SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = engine_url(app.config['DATABASE'])
    db.init_app(app)

    # Blueprints
    blueprints.register_blueprints(app)

    # Sass
    with app.app_context():
        app.scss = ScssMiddleware(scss_dir=resource.get_resource('scss'),
                                  css_dir=os.path.join(tempfile.gettempdir(),
                                                       'fourm_gun', 'css'),
                                  app=app)
    # Jinja configurations
    @app.context_processor
    def inject_globals():
        return {
            'm': m,
            'models': m,
            'db': db,
        }

    return app