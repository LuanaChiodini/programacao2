from flask import Flask, render_template, request, redirect, session
import os
from peewee import *
from modelo import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "2243"
pessoas = []

@app.route("/")
def inicio():
	return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html", lista=Pessoa.select())

@app.route("/cadastrar_pessoa", methods=["POST"])
def casdastrar_pessoa():
	nome = request.form["nome"]
	endereco = request.form["endereco"]
	cpf = request.form["cpf"]
	Pessoa.create(nome=nome,
				endereco=endereco,
				cpf=cpf)
	return render_template("exibir_mensagem.html", mensagem="cadastro concluído", pessoa=(nome,endereco,cpf))

@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
	return render_template("/form_inserir_pessoa.html")

@app.route("/form_excluir_pessoa")
def form_excluir_pessoa():
	if session["usuario"]:
		id = request.args.get("id")
		Pessoa.delete_by_id(request.args.get("id"))
		return render_template("exibir_mensagem.html", mensagem="pessoa excluída")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
	id = request.args.get("id")
	for p in pessoas:
		if p.id == id:
			return render_template("form_alterar_pessoa.html", informacao=p)
	return "pessoa não encontrada"

@app.route("/alterar_pessoa")
def alterar_pessoa():
	id = request.form["id"]
	nome = request.form["nome"]
	endereco = request.form["endereco"]
	cpf = request.form["cpf"]
	cidadao = Pessoa.get_by_id(request.form["id"])
	cidadao.nome = nome
	cidadao.endereco = endereco
	cidadao.cpf = cpf
	cidadao.save()
	return redirect("/listar_pessoas")

@app.route("/form_login")
def form_login():
	return render_template("form_login.html")

@app.route("/login", methods=["POST"])
def login():
	login = request.form["login"]
	senha = request.form["senha"]
	if login == "luana" and senha == "1234":
		session["usuario"] = login
		return redirect("/")
	else:
		return render_template("exibir_mensagem.html", mensagem="login e/ou senha inválidos")

@app.route("/logout")
def logout():
	session.pop("usuario")
	return redirect("/")

app.run(debug=True, host="0.0.0.0")
