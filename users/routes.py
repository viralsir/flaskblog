from flask import Blueprint,render_template

user=Blueprint('user',__name__)

@user.route("/register")
def register():
    return render_template("user/register.html")
