from flask import Flask, request, redirect, url_for, session, render_template_string, render_template
import os
app = Flask(__name__)

app.secret_key = "your_secret_key"  # Задайте секретный ключ для сессий

# Задайте правильные логин и пароль
USERNAME = "admin"
PASSWORD = "password123"


@app.route("/", methods=["GET", "POST"])
def login():
    """Страница логина с подключением stylesLogin.css"""
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            session["authenticated"] = True  # Устанавливаем флаг аутентификации
            return redirect(url_for("welcome"))
        else:
            error = "Неправильный логин или пароль"
    return render_template("login.html")


@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    """Главная страница с подключением stylesMain.css"""
    if not session.get("authenticated"):
        return redirect(url_for("login"))

    return render_template("main.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":
        full_name = request.form.get("full_name")
        age = request.form.get("age")
        birth_date = request.form.get("birth_date")
        return redirect(url_for("profile", name=full_name, age=age, birth_date=birth_date))


    return render_template("upload.html")


@app.route("/view")
def view():
    return render_template("view.html")




@app.route("/profile")
def profile():
    """Страница профиля пользователя с подключением stylesProfile.css"""
    name = request.args.get("name")
    age = request.args.get("age")
    birth_date = request.args.get("birth_date")


    return render_template("profile.html", name=name, age=age, birth_date=birth_date)


if __name__ == "__main__":
    app.secret_key = "your_secret_key"  # Убедитесь, что ключ безопасный
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
