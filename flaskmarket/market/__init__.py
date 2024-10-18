from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
load_dotenv()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:*Oluwaseyi123@localhost/OluwaseyiTest"
app.config['SECRET_KEY'] = '03489a14bcf9f88f1b3b5ccd'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
mysql = MySQL(app=app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import models

with app.app_context():
    db.create_all()


from market import routes
###class model
# class Items(db.Model):
#     id = db.Column(db.Integer(), nullable = False, primary_key = True)
#     name = db.Column(db.String(30), nullable=False, unique=True)
#     price = db.Column(db.Integer(), nullable=False)
#     backcode = db.Column(db.String(12), nullable=False, unique=True)
#     description = db.Column(db.String(225), nullable=False, unique=True)


#     ##how to dispaly your table or query
#     ## this will reutn something like [Items name1, Items name2, Items name3]
#     def __repr__(self):
#         return f'Items {self.name}'

# with app.app_context():
#     db.create_all()


# @app.route('/')
# def home_page():
#     return render_template('home.html')

# @app.route('/market')
# def market_page():
#     items = Items.query.all
#     return render_template('market.html', items = items)





