from peewee import *

arq = ":memory"
db = SqliteDatabase

class BaseModel(Model):
	class Meta():
		database = db

class Pessoa(BaseModel):
	nome = CharField()
	endereco = CharField()
	telefone = CharField()
	email = CharField()

if __name__ == "__main__":
	db.connect()
	db.create_tables([Pessoa])
	luana = Pessoa.create(nome="Luana Chiodini", endereco="Casa linda", telefone="1111-1111", email="aaa@gmail.com")
	todos = luana.select()
	for i in range(todos):
		print(i)