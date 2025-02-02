from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(),
        Length(min=3, max=25, message="Username must be between 3 and 25 characters.")
    ])
    
    email = StringField("Email", validators=[
        DataRequired(),
        Email(message="Invalid email format."),
        Regexp(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", message="Enter a valid email.")
    ])
    
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long."),
        Regexp(r"^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[a-z\d@$!%*?&]{8,}$", 
               message="Password must contain at least one lowercase letter, one digit, and one special character.")
    ])
    
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(),
        EqualTo("password", message="Passwords must match.")
    ])
    
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(),
        Email(message="Invalid email format.")
    ])
    
    password = PasswordField("Password", validators=[DataRequired()])
    
    submit = SubmitField("Login")