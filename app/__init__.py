from flask import Flask
import os

def designing_app():
    app = Flask(__name__)
    app.secret_key = 'super-secret'
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    from .routes import main
    app.register_blueprint(main)
    return app