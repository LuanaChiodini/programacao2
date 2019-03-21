from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("inicio.html")

pessoas = []

class Pessoa():
	def __init__(self, nome, endereco, telefone):
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html", lista=pessoas)

@app.route("/cadastrar_pessoa")
def adicionar():
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	telefone = request.args.get("telefone")
	pessoas.append(Pessoa(nome, endereco, telefone))
	return render_template("exibir_mensagem.html", pessoa=(nome,endereco,telefone)) 

@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
	return render_template("form_inserir_pessoa.html")

@app.route("/form_excluir_pessoa")
def form_excluir_pessoa():
	return render_template("form_excluir_pessoa.html")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
	return render_template("form_alterar_pessoa.html")

@app.route("/exibir_mensagem")
def exibir_mensagem():
	return render_template("exibir_mensagem.html")

app.run(debug=True, host="0.0.0.0")