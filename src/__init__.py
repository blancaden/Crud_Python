from flask import Flask;

from .routes import ClienteRouter

app= Flask(__name__)

def init__app(config):
    app.config.from_object(config)

    app.register_blueprint(ClienteRouter.main, url_prefix='/Cliente')
    return app