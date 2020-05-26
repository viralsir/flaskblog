from flask_wtf.form import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from users.model import User

class RegisterForm(FlaskForm):
    username=StringField("User Name :",validators=[DataRequired()])
    email=StringField("Email ",validators=[DataRequired(),Email()])
    password=PasswordField("Password :",validators=[DataRequired(),Length(min=2,max=16)])
    confirm_password=PasswordField("Confirm Password :",validators=[DataRequired(),Length(min=2,max=16),EqualTo('password')])
    signup=SubmitField('Sign Up')

    def validate_email(selfs,email):
        user=User.query.filter_by(email=email.data).first()
        if user :
            raise  ValidationError('Email is already taken plase choose another one')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user :
            raise ValidationError('Username is already taken please choose another one ')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),])
    submit=SubmitField('Log in')
    remember_me=BooleanField("Remember me")


