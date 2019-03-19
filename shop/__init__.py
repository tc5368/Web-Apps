from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '427d256a73d6122069cb10b8f94a46dd9f6675afbf09baaf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1769261:apmWzUswLy6LvfX@csmysql.cs.cf.ac.uk:3306/c1769261'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from shop import routes
