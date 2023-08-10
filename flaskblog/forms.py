from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length,  Email, EqualTo, ValidationError
from email_validator import validate_email
from flaskblog.models import User




class RegistraionForm(FlaskForm):

    username=StringField('Username', 
                        validators=[DataRequired(), Length(min=5, max=22) ])

    email=StringField('Email',
                        validators=[DataRequired(), Email()])

    password=PasswordField('Password', 
                        validators=[DataRequired(),Length(min=5, max=20)] )

    confirm_password=PasswordField('Confirm Password', 
                        validators=[DataRequired(),Length(min=5, max=20), EqualTo('password')])

    submit=SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken. Please choose a different one')


class LoginForm(FlaskForm):

    email=StringField('Email',
                        validators=[DataRequired(), Email()])

    password=PasswordField('Password', 
                        validators=[DataRequired(),Length(min=5, max=20)])

    remember= BooleanField('Remember Me ')

    submit=SubmitField('Log In')


class UpdateAccountForm(FlaskForm):

    username=StringField('Username', 
                        validators=[DataRequired(), Length(min=5, max=22) ])

    email=StringField('Email',
                        validators=[DataRequired(), Email()])
    
    picture=FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])

    submit=SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already taken. Please choose a different one')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already taken. Please choose a different one')
