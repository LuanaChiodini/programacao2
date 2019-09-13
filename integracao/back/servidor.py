from flask import Flask, jsonify
from modelo import Pessoa 
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__)

@app.route("/")
def index():
	return "backend do sistema pessoas; <a href=/listar_pessoas>API listar pessaos</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
	pessoas = list(map(model_to_dict, Pessoa.select()))
	return jsonify({"lista":pessoas})

app.run(debug=True, port=4999)	