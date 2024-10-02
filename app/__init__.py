from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config  # Import the configuration file
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)  
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import register_blueprints
register_blueprints(app)
