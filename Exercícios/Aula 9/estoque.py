class Pessoa():
    def __init__(self, nome):
        self.nome = nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        Pessoa.__init__(self, nome)
        self.cpf = cpf
    
    def setCPF(self, cpf):
        self.cpf = cpf
    
    def getCPF(self):
        return self.cpf
    
class Fornecedor(Pessoa):
    def __init__(self, nome, cnpj):
        Pessoa.__init__(self, nome)
        self.cnpj = cnpj
    
    def setCNPJ(self, cnpj):
        self.cnpj = cnpj
    
    def getCNPJ(self):
        return self.cnpj

class Transacao():
    def __init__(self, dataTransacao, produto, qtde):
        self.dataTransacao = dataTransacao
        self.produto = produto
        self.qtde = qtde
    
    def setDataTransacao(self, dataTransacao):
        self.dataTransacao = dataTransacao
    
    def getDataTransacao(self):
        return self.dataTransacao
    
    def setProduto(self, produto):
        self.produto = produto
    
    def getProduto(self):
        return self.produto

    def setQtde(self, qtde):
        self.qtde = qtde
    
    def getQtde(self):
        return self.qtde
        
#(1)
class Produto():
    def __init__(self, nome, qtdeEstoque, precoUnit, estoqueMinimo, estoqueMaximo):
        self.nome = nome
        self.qtdeEstoque = qtdeEstoque
        self.precoUnit = precoUnit
        self.estoqueMinimo = estoqueMinimo
        self.estoqueMaximo = estoqueMaximo
        self.historico = []
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setQtdeEstoque(self):
        self.qtdeEstoque = qtdeEstoque
    
    def getQtdeEstoque(self):
        return self.qtdeEstoque
    
    def setPrecoUnit(self, precoUnit):
        self.precoUnit = precoUnit
    
    def getPrecoUnit(self):
        return self.precoUnit
    
    def setEstoqueMinimo(self):
        self.estoqueMinimo = estoqueMinimo
    
    def getEstoqueMinimo(self):
        return self.estoqueMinimo
    
    def setEstoqueMaximo(self, estoqueMaximo):
        self.estoqueMaximo = estoqueMaximo
    
    def getEstoqueMaximo(self):
        return self.estoqueMaximo
    
    #(A)
    def debitarEstoque(self, quantidade):
        self.qtdeEstoque -= quantidade
    
    #(B)
    def creditarEstoque(self, quantidade):
        self.qtdeEstoque += quantidade
    
    #(C)
    def verificarEstoqueBaixo(self):
        return self.qtdeEstoque < self.estoqueMinimo
    
    #(D)
    def verificarEstoqueInsuficiente(self, quantidade):
        return self.qtdeEstoque < quantidade
    
    #(E)
    def verificarEstoqueExcedente(self, quantidade):
        return (self.qtdeEstoque + quantidade) > self.estoqueMaximo

    #(F)
    def calcularValorVenda(self, quantidade):
        return self.precoUnit * quantidade

    #(G)
    def vender(self, dataVenda, cliente, qtdeVendida):
        if self.verificarEstoqueInsuficiente(qtdeVendida):
            print("Estoque Insuficiente!")
            return False
        venda = Venda(self, dataVenda, cliente, qtdeVendida)
        self.debitarEstoque(qtdeVendida)
        valorVenda = self.calcularValorVenda(qtdeVendida)
        print(f"Valor venda = {valorVenda}")
        self.registrarHistorico(f"Venda do produto {self.nome}")
        if self.verificarEstoqueBaixo():
            print("Estoque Baixo")
        return venda
    
    #(H)
    def comprar(self, dataCompra, fornecedor, qtdeCompra, precoUnit):
        if self.verificarEstoqueExcedente(qtdeCompra):
            print("Estoque Excedente")
            return False
        compra = Compra(self, dataCompra, fornecedor, qtdeCompra, precoUnit)
        self.creditarEstoque(qtdeCompra)
        self.registrarHistorico(f"Compra do produto {self.nome}")
        return compra
    
    #(I)
    def registrarHistorico(self, transacao):
        self.historico.append(transacao)
    
    #(J)
    def exibirHistorico(self):
        for registro in self.historico:
            print(registro)
    
#(2)
class Compra(Transacao):
    def __init__(self, dataCompra, produto, fornecedor, qtdeCompra, precoUnit):
        Transacao.__init__(self, dataCompra, produto, qtdeCompra)
        self.fornecedor = fornecedor
        self.precoUnit = precoUnit
    
    def setFornecedor(self, fornecedor):
        self.fornecedor = fornecedor
    
    def getFornecedor(self):
        return self.fornecedor
    
    def setPrecoUnit(self, precoUnit):
        self.precoUnit = precoUnit
    
    def getPrecoUnit(self):
        return self.precoUnit
    
    #(A)
    def comprar(self, produto, qtdeCompra):
        if produto.verificarEstoqueExcedente(qtdeCompra):
            print("Estoque Excedente!")
            return False
        produto.creditarEstoque(qtdeCompra)
        return True

#(3)
class Venda(Transacao):
    def __init__(self, dataVenda, cliente, produto, qtdeVendida):
        Transacao.__init__(self, dataVenda, produto, qtdeVendida)
        self.cliente = cliente
    
    def setCliente(self, cliente):
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente
    
    #(A)
    def vender(self, produto, qtdeVendida):
        if self.verificarEstoqueInsuficiente(qtdeVendida):
            print("Estoque Insuficiente!")
            return False
        produto.debitarEstoque(qtdeVendida)
        produto.registrarHistorico(f"Venda de produto {produto.nome}")
        if produto.verificarEstoqueBaixo():
            print("Estoque Baixo")
        return True

cliente = Cliente("Marco", "14062024140")
produto = Produto("Caneta", 100, 1.2, 10, 200)
produto.vender("14/06/2024", cliente, 95)

fornecedor = Fornecedor("Antônio", "14062024000600")
produto.comprar("14/06/2024", fornecedor, 50, 1.1)
produto.exibirHistorico()


    

