import os
from peewee import *

arq = "pessoa.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Pessoa(BaseModel):
	nome = CharField()
	endereco = CharField()
	cpf = CharField()

if __name__ == "__main__":
	
	if os.path.exists(arq):
		os.remove(arq)

	try:
		db.connect()
		db.create_tables([Pessoa])

	except OperationError as erro:
		print("erro ao criar as tabelas")