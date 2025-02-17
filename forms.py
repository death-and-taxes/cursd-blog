'''
This file stores web form classes. See Grinberg chap 3 
The LoginForm class is used by app/templates/login.htmls
'''
from flask_wtf import FlaskForm
from wtforms import String Field, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username"' validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
