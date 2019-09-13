from peewee import *

arq = "./pessoas-front-end.db"
db = SqliteDatabase

class BaseModel(Model):
	class Meta():
		database = db

class Pessoa(BaseModel):
	nome = CharField()
	endereco = CharField()
	telefone = CharField()

if __name__ == "__main__":
	db.connect()
	db.create_tables([Pessoa])
	luana = Pessoa.create(nome="Luana Chiodini", endereco="Casa linda", telefone="1111-1111")
	todos = luana.select()
	for i in range(todos):
		print(i)