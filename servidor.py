import Flask, render_template, request

class Pessoa():
	def __init__(self, nome, endereco, cpf):
		self.nome = nome
		self.endereco = endereco
		self.cpf = cpf

app = Flask(__name__)
pessoas = []

@app.route("/")
def inicio():
	return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar():
	return render_template("listar_pessoas.html", lista=pessoas)

@app.route("/cadastrar_pessoa")
def casdastrar_pessoa():
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	cpf = request.args.get("cpf")
	pessoas.append(Pessoa(nome, endereco, cpf))
	return render_template("exibir_mensagem.html", mensagem="cadastro concluído", pessoa=(nome,endereco,cpf))

@app.route("/form_alterar_pessoa")
def alterar_pessoa():
	return render_template("exibir_mensagem.html", mensagem="pessoa alterada")

@app.route("/form_excluir_pessoa")
def excluir_pessoa():
	achou = None
	cpf = request.args.get("cpf")
	for p in pessoas:
		if p.cpf == cpf:
			pessoas.remove(achou)
	return render_template("exibir_mensagem.html", mensagem="pessoa excluída")

app.run()

app = run(debug=True, host="0.0.0.0")