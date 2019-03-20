from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("inicio.html")

class Pessoa():
	def __init__(self, nome, rua, telefone):
		self.nome = nome
		self.rua = rua
		self.telefone = telefone

@app.route("/listar_pessoas")
def listar_pessoas():
	pessoas = [ Pessoa("Luana", "Alex Robe", "9161-9082"),
				Pessoa("Grazi", "Frederico Jesen", "9911-2233")
	]
	print(pessoas)
	return render_template("listar_pessoas.html", lista=pessoas)


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