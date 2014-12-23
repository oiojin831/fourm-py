# -*- encoding: utf-8 -*-
"""
"""
import menu, main, insta, login

def register_blueprints(app):
    app.register_blueprint(menu.blueprint)
    app.register_blueprint(main.blueprint)
    app.register_blueprint(login.blueprint)
    app.register_blueprint(insta.blueprint)