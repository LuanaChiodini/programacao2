class Pessoa():
	def __init__(self, nome, rua, telefone):
		self.nome = nome
		self.rua = rua
		self.telefone = telefone

if __name__ == "__main__":
	pessoa = Pessoa("Maria", "rua", "1111-1111") 
	print(pessoa.nome, pessoa.rua, pessoa.telefone)