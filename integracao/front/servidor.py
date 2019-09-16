from flask import Flask, render_template, request, redirect, session
from modelo import Pessoa
import requests
from playhouse.shortcuts import model_to_dict, dict_to_dict

app = Flask(__name__)

@app.route("/")
def inicio():
	return "frontend do sistema de pessoa. <a href=/listar_pessoas>Operação listar</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
	dados_pessoas = requests.get("http://localhost:4999/listar_pessoas")
	json_pesssoas = dados_pessoas.json()
	pessoas = []
	for pessoa_em_json in json_pesssoas["lista"]:
		p = dict_to_model(Pessoa, pessoa_em_json)
		pessoas.append(p)
	return render_template("listar_pessoas.html", lista=pessoas)

app.run(debug=True)	