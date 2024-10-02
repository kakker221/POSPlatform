from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config  # Import the configuration file
from flask_migrate import Migrate


# Initialize app and db
app = Flask(__name__)
app.config.from_object(Config)  # Load configuration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes after app and db are initialized
from app.routes import register_blueprints
register_blueprints(app)
