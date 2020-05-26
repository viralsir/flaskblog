from flask import Blueprint,render_template,flash,redirect,url_for
from users.form import  RegisterForm,LoginForm
from main import bcrypt,db
from users.model import User
from flask_login import login_user,logout_user,current_user

user=Blueprint('user',__name__)

@user.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated :
        return redirect(url_for('home'))
    form=RegisterForm()
    if form.validate_on_submit() :
        hash_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user=User(username=form.username.data,email=form.email.data,password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f"'{form.username} is created you can login now ","success")
        return redirect(url_for('user.login'))

    return render_template("user/register.html",title="Register",form=form)

@user.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()

    if form.validate_on_submit() :
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember_me.data)
            flash("Login successfully ","success")
            return redirect(url_for("home"))
        else :
            flash("Username or password is incorrect","danger")

    return render_template("user/login.html",title="Login",form=form)


@user.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"));
