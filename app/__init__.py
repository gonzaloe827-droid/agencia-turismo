
from flask import Flask
from .extensions import appbuilder, db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    with app.app_context():
        # Importar los modelos
        from . import models

        # Inicializar Flask-AppBuilder
        appbuilder.init_app(app, db.session)

        # Registrar las vistas
        from . import views

    return app


app = create_app()
