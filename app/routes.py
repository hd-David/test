from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import db, login_manager
from .models import User
from .forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main.route('/')
def home():
    return render_template('landing.html')

@main.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if the username or email already exists in the database
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()
        
        if existing_user:
            # Check which field is causing the conflict
            if existing_user.username == form.username.data:
                flash('This username is already taken. Please choose another.', 'danger')
            elif existing_user.email == form.email.data:
                flash('This email is already registered. Please log in or use a different email.', 'danger')
            return render_template('register.html', form=form)

        # If no conflicts, create the user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        try:
            db.session.commit()
            flash('Account created successfully! Please log in.', 'success')
            print("Redirecting to login...")  # Debug print
            return redirect(url_for('main.login'))
        except Exception as e:
            print(f"Error during registration: {e}")  # Debug print
            db.session.rollback()
            flash('An unexpected error occurred. Please try again later.', 'danger')

    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Welcome back!', 'success')
            return redirect(url_for('main.dashboard'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)