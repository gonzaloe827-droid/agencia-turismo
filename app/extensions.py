from flask_sqlalchemy import SQLAlchemy
from flask_appbuilder import AppBuilder
from flask_appbuilder.models.sqla import Model

db = SQLAlchemy(model_class=Model)
appbuilder = AppBuilder()