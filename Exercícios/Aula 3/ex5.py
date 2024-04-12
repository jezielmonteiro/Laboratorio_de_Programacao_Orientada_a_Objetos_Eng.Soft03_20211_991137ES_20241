#Classe Produto:

#Atributos: nome, preco, quantidade_estoque, categoria
#Métodos: adicionar_estoque, remover_estoque, aplicar_desconto
#• adicionar_estoque(quantidade): Adiciona quantidade ao quantidade_estoque.
#• remover_estoque(quantidade): Remove quantidade do quantidade_estoque, se
#houver quantidade suficiente.
#• aplicar_desconto(percentual): Aplica um desconto de percentual ao preco do
#produto.


class Produto:
    def __init__(self):
        self.nome = ""
        self.preco = 0.0
        self.quantidade = 0
        self.categoria = ""

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setPreco(self, preco):
        self.preco = preco

    def getPreco(self):
        return self.preco
    
    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getQuantidade(self):
        return self.quantidade

    def setCategoria(self, categoria):
        self.categoria = categoria

    def getCategoria(self):
        return self.categoria

    def adicionarEstoque(self, quantidade):
        self.quantidade += quantidade
    
    def removerEstoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade

    def aplicarDesconto(self, percentual):
        if percentual >= 0 and percentual <= 100:
            self.preco = self.preco - (self.preco * (percentual / 100))

produto = Produto()

produto.setNome("Logitech G PRO Wireless")
print(produto.getNome())
produto.setCategoria("Informática")
print(produto.getCategoria())
produto.setPreco(550)
print(produto.getPreco())
produto.setQuantidade(1500)
print(produto.getQuantidade())
produto.adicionarEstoque(500)
print(produto.getQuantidade())
produto.removerEstoque(500)
print(produto.getQuantidade())
produto.aplicarDesconto(40)
print(produto.getPreco())
