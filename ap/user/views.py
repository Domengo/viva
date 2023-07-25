from flask import render_template, url_for, flash, redirect, request
from viva.ap.user import user
from viva.ap.user.forms import RegistrationForm, LoginForm
from viva.ap import db


def get_User():
    from viva.ap.user.models import User  # delay the import of User
    return User


@user.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    User = get_User()
    
    if form.validate_on_submit():
        hashed_password = User.generate_password_hash(form.password.data)
        db_user = User(fullname=form.fullname.data, username=form.username.data, email=form.email.data, password=hashed_password, phone=form.phone.data)
        db.session.add(db_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('user.login'))
    return render_template('templates/signup2.html', title='register', form=form)

@user.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    User = get_User()

    if form.validate_on_submit():
        db_user = User.query.filter_by(email=form.email.data).first()
        if db_user and db_user.check_password(form.password.data):
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
