import os
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)
    
    @app.route('/')
    def index():
        return redirect(url_for('scrapple'))

    @app.route('/scrapple/')
    def scrapple(word=None):
        return render_template('word_search.html.jinja', word=word)


    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html.jinja'), 404
    
    
    return app




