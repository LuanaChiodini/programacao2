from flask import Flask, render_template, request, redirect, session
from modelo import Pessoa
import requests
from playhouse.shortcuts import model_to_dict, dict_to_dict

app = Flask(__name__)

@app.route("/")
def inicio():
	return "frontend do sistema de pessoa. <a href=/listar_pessoas>Operação listar</a>"

@app.route("/listart")