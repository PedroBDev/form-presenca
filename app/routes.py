from flask import render_template, session, request, redirect, url_for, flash
from app import app
from app.forms import PresencaForm
from .utils import ler_presenca 

@app.route("/", methods = ["GET", "POST"])
def homepage():
    form = PresencaForm()
    if form.validate_on_submit():
        form.save()
    return render_template("index.html", form = form)


@app.route("/admin", methods = ["GET", "POST"])
def admin():
    if request.method=="POST":
        senha = request.form.get("senha")
        if senha==app.config["ADMIN_PASSWORD"]:
            session["admin"]=True
            return redirect(url_for("informacoes"))
        else:
            flash("ACESSO NEGADO:SENHA INCORRETA", "danger")
            return redirect(url_for("homepage"))
    return render_template("admin.html")

@app.route("/informacoes")
def informacoes():
    presenca = ler_presenca()
    return render_template("lista.html", presencas = presenca)