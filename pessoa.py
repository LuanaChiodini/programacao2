class Pessoa():
	def __init__(self, nome, endereco, telefone):
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone

if __name__ == "__main__":
	pessoa = Pessoa("Maria", "rua", "1111-1111") 
	print(pessoa.nome, pessoa.endereco, pessoa.telefone)