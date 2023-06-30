# take note all this library
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# a hash is a function with no inverse
from . import db 
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user : 
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else :
                flash('Incorrect password, try again.', category='error')
        else :
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()

@auth.route('/logout')
@login_required # make sure u only logout when you are currently login
def logout():
    clear_data(db.session)
    # db.session.delete(current_user)
    db.session.commit()
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4: 
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            # way to use ' in string
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:  
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            # sha256 is a hash algorithm 
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True) 
            # fuckingggggg error !!!!
            flash('Account created!', category='success')   
            # url_for : whenever you change the url you don't have to change function name you wanna go to
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
