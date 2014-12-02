# -*- encoding: utf-8 -*-
"""
"""
import menu, main

def register_blueprints(app):
    app.register_blueprint(menu.blueprint)
    app.register_blueprint(main.blueprint)