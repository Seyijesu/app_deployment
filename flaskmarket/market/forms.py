from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, ValidationError, DataRequired
from market.models import Users

class RegisterForm(FlaskForm):

    def validate_userName(self, username_to_check):
        user = Users.query.filter_by(userName=username_to_check.data).first()
        if user:
            raise ValidationError("Username Already Exist")
        
    def validate_email(self, email_to_check):
        user = Users.query.filter_by(emailAddress=email_to_check.data).first()
        if user:
            raise ValidationError("Email Adress Already Exist")

    username = StringField(label="User Name", validators=[Length(min=2, max=30)])
    email = StringField(label = "Email Address", validators=[Email()])
    password1 = PasswordField(label = "Password", validators= [Length(min=6)])
    password2 = PasswordField(label= "Comferm Password", validators = [EqualTo('password1')])
    submit = SubmitField(label = "Create Account")

class LoginForm(FlaskForm):
    username = StringField(label = "Username", validators=[DataRequired()]) 
    password = PasswordField(label = "Password", validators=[DataRequired()]) 
    submit = SubmitField(label="Sign in")

class PurcahseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')