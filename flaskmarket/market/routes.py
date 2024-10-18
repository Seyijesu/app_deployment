from flask import render_template, redirect, url_for, flash, request
from market import app
from market.models import Items, Users
from market.forms import RegisterForm, LoginForm, PurcahseItemForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/market', methods=["POST", "GET"])
@login_required
def market_page():
    purchase_form = PurcahseItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchase_item')
        p_item_object = Items.query.filter_by(name = purchased_item)
        if p_item_object:
            p_item_object.owner = current_user.id
            current_user.budget -= p_item_object.price
            db.session.commit()
    items = Items.query.all()
    return render_template('market.html', items = items,  purchase_form=purchase_form)

@app.route("/register", methods=["POST", 'GET'])
def register_page():
    form = RegisterForm()

    ##Validation
    if form.validate_on_submit():

        ## Create Instance of User
        user_to_create = Users(userName = form.username.data, emailAddress= form.email.data, password = form.password1.data)

        ## To affect the changes in database
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f"Account Create Successfully as {user_to_create.userName}", category="success")
        
        return redirect(url_for('market_page'))
    
    ##If there are no errors in the form
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error in this form: {err_msg}", category = 'danger')
    return render_template("register.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login_page():

    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(userName=form.username.data).first()
        print(attempted_user.passwordHash)
        if attempted_user and attempted_user.check_password_correction(attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f"Success! You are now logged in as {attempted_user.userName}", category="success")
            return redirect(url_for("market_page"))
        else:
            flash(f"Username and password are not match! Please try again", category='danger')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash(f"You have been logged out", category='info')
    return redirect(url_for("home_page"))