# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, request

blueprint = Blueprint('login', __name__)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] !='admin':
            error = 'Invalid credentials, Please try again.'
        else:
            return redirect(url_for('main.main'))
    return render_template('login.html', error=error)