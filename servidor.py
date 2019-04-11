from flask import Flask, render_template, request, redirect

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

@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
	return render_template("/form_inserir_pessoa.html")

@app.route("/form_excluir_pessoa")
def form_excluir_pessoa():
	cpf = request.args.get("cpf")
	for p in pessoas:
		if p.cpf == cpf:
			pessoas.remove(p)
	return render_template("exibir_mensagem.html", mensagem="pessoa excluída")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
	cpf = request.args.get("cpf")
	for p in pessoas:
		if p.cpf == cpf:
			return render_template("form_alterar_pessoa.html", informacao=p)
	return "pessoa" + p + "excluída"

@app.route("/alterar_pessoa")
def alterar_pessoa():
	procurado = request.args.get("cpf_original")
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	cpf = request.args.get("cpf")
	nova_pessoa = Pessoa(nome, endereco, cpf)
	for i in range(len(pessoas)):
		if pessoas[i].cpf == procurado:
			pessoas[i] = nova_pessoa
			return redirect("/listar_pessoas")
	return "pessoa não encontrada"

app.run(debug=True, host="0.0.0.0")
