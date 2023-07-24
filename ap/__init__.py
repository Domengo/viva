from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .user.views import user
import os, dotenv

dotenv.load_dotenv()

# Database configuration
event_user = os.getenv('eventU')
event_pwd = os.getenv('pwd')
event_host = os.getenv('host')
event_db = os.getenv('db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{event_user}:{event_pwd}@{event_host}/{event_db}'
SECRET_KEY = os.getenv('SECRET_KEY') or 'hard to guess string'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['PROPAGATE_EXCEPTIONS'] = True

app.register_blueprint(user)


db = SQLAlchemy(app)
