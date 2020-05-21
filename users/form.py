from flask_wtf.form import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegisterForm(FlaskForm):
    username=StringField("User Name :",validators=[DataRequired()])
    email=StringField("Email ",validators=[DataRequired(),Email()])
    password=PasswordField("Password :",validators=[DataRequired(),Length(min=2,max=16)])
    confirm_password=PasswordField("Confirm Password :",validators=[DataRequired(),Length(min=2,max=16),EqualTo(password)])
    signup=SubmitField('Sign Up')




