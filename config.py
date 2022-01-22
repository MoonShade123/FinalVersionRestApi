import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Connexion app creation
connex_app = connexion.FlaskApp(__name__, specification_dir=basedir,
                                arguments={'global': 'global_value'})

# Base flask app instance
app = connex_app.app

# SQL url
sqlite_url = "sqlite:///" + os.path.join(basedir, "post.db")

# Configuration
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db instance
db = SQLAlchemy(app)

# Marshmellow init
ma = Marshmallow(app)
