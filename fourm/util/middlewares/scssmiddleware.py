import os
import codecs
import shutil
import posixpath

from scss import Scss
from flask import Blueprint, abort, send_file, url_for

def _convert(src, dst):
    css = Scss()
    with codecs.open(src, 'r', encoding='utf-8') as f:
        source = f.read()

    output = css.compile(source)

    with codecs.open(dst, 'w', encoding='utf-8') as f:
        f.write(output)

class ScssMiddleware(object):
    def __init__(self, scss_dir, css_dir, app=None, force=False,
                 blueprint_name='scss', blueprint_prefix='/scss/compiled'):

        super(ScssMiddleware, self).__init__()
        self.scss_dir = scss_dir
        self.css_dir = css_dir
        self.force = force

        blueprint = Blueprint(blueprint_name, __name__)

        @blueprint.route('/<path:css_path>')
        def css(css_path):
            if not css_path.endswith('.css'):
                abort(404)
            path = css_path[:-len('.css')]
            path_components = posixpath.split(path)

            scss_path = os.path.join(self.scss_dir, *path_components) + '.scss'
            css_path = os.path.join(self.css_dir, *path_components) + '.css'

            if not os.path.isfile(scss_path):
                abort(404)
            if (self.force or not os.path.isfile(css_path) or
                    os.path.getmtime(scss_path) >
                    os.path.getmtime(css_path)):
                css_parent = os.path.dirname(css_path)
                if not os.path.exists(css_parent):
                    os.makedirs(css_parent)
                cwd = os.path.dirname(scss_path)

                original_wd = os.getcwd()
                try:
                    os.chdir(cwd)
                    _convert(scss_path, css_path)
                finally:
                    if os.getcwd() != original_wd:
                        os.chdir(original_wd)
                app.logger.debug('Compiled %s into %s' % (scss_path, css_path))
            return send_file(css_path)

        self.blueprint = blueprint
        self.blueprint_prefix = blueprint_prefix

        if app is not None:
            self.init_app(app)
        else:
            self.app = None

    def init_app(self, app):
        self.app = app
        self.app.register_blueprint(self.blueprint,
                                    url_prefix=self.blueprint_prefix)
        if os.path.exists(self.css_dir):
            shutil.rmtree(self.css_dir)

        @app.context_processor
        def inject_globals():
            return {
                'scss_url': self.scss_url
            }

    def scss_url(self, scss_path, **kwargs):
        if scss_path.endswith('.scss'):
            path = scss_path[:-len('.scss')]
        else:
            path = scss_path
        path_components = posixpath.split(path)
        css_uri = posixpath.join(*path_components) + '.css'

        return url_for(self.blueprint.name + '.css', css_path=css_uri)