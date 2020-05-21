from flask import Blueprint

user=Blueprint('user',__name__)

@user.route("/register")
def register():
    return "<h1>Register Page</h1>"

