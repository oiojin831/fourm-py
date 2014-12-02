# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('menu', __name__)

@blueprint.route('/menu')
def menu():
    return render_template('menu.html')