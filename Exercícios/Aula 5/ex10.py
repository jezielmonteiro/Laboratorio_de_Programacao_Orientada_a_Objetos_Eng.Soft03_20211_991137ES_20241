#Classes: Produto, Livro, Eletrônico

#Produto: nome, preço, método para aplicar desconto
#Livro: autor, método para aplicar desconto (5% adicional)
#Eletrônico: garantia, método para aplicar desconto (10% adicional)


class Produto:
    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.desconto = 0
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setPreco(self, preco):
        self.preco = preco
    
    def getPreco(self):
        return self.preco
    
    def setDesconto(self, desconto):
        self.desconto = desconto
    
    def getDesconto(self):
        self.preco = self.preco - (self.preco * self.desconto)
        return self.preco
    
class Livro(Produto):
    def __init__(self):
        Produto.__init__(self)
        self.autor = ""
    
    def setAutor(self, autor):
        self.autor = autor

    def getAutor(self):
        return self.autor
    
class Eletronico(Produto):
    def __init__(self):
        Produto.__init__(self)
        self.garantia = ""
    
    def setGarantia(self, garantia):
        self.garantia = garantia

    def getGarantia(self):
        return self.garantia

livro = Livro()

livro.setNome("Programação Orientada a Objetos")
print(livro.getNome())
livro.setPreco(200)
print(livro.getPreco())
livro.setAutor("Marco Antônio")
print(livro.getAutor())
livro.setDesconto(10 / 100)
print(livro.getDesconto())


eletronico = Eletronico()

eletronico.setNome("Notebook Acer")
print(eletronico.getNome())
eletronico.setPreco(3500)
print(eletronico.getPreco())
eletronico.setGarantia("3 anos")
print(eletronico.getGarantia())
eletronico.setDesconto(40 / 100)
print(eletronico.getDesconto())