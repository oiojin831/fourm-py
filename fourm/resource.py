# -*- encoding: utf-8 -*-

import os

from flask import current_app as app

def resource_directory(root_path=None):
    if root_path is None:
        try:
            root_path = app.root_path
        except RuntimeError:
            root_path = os.path.dirname(__file__)
    return os.path.join(root_path, 'resources')

def get_resource(filename, root_path=None):
    return os.path.join(resource_directory(root_path), filename)

def open_resource(filename, mode='r', root_path=None):
    return open(get_resource(filename, root_path=root_path), mode=mode)

def has_resource(filename, root_path=None):
    return os.path.exists(get_resource(filename, root_path=root_path))