from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin




@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    userName = db.Column(db.String(30), nullable=False, unique=True)
    emailAddress = db.Column(db.String(225), nullable=False, unique=True)
    passwordHash = db.Column(db.String(150), nullable=False)
    budget = db.Column(db.Integer, server_default="1000", nullable=False)
    items = db.relationship("Items", backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.passwordHash = bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.passwordHash, attempted_password)
    
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'


###class model
class Items(db.Model):
    id = db.Column(db.Integer(), nullable = False, primary_key = True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    description = db.Column(db.String(225), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    ##how to dispaly your table or query
    ## this will reutn something like [Items name1, Items name2, Items name3]
    def __repr__(self):
        return f'Items {self.name}'
    

