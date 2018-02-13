from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SignupForm(FlaskForm):
    user = StringField('User Name')
    submit = SubmitField('Sign Up')


class ChatForm(FlaskForm):
    user = StringField('User Name')
    message = StringField('Message')
    submit = SubmitField('Send')
