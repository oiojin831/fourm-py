# -*- encoding: utf-8 -*-
"""
"""
import menu, main, insta, auth

def register_blueprints(app):
    app.register_blueprint(menu.blueprint)
    app.register_blueprint(main.blueprint)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(insta.blueprint)