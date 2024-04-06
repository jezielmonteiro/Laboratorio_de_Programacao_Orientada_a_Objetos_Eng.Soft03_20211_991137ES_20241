#Classes: Pessoa, Pessoa Física, Pessoa Jurídica

#Pessoa: nome, endereco
#Pessoa Física: cpf
#Pessoa Jurídica: cnpj


class Pessoa:
    def __init__(self):
        self.nome = ""
        self.endereco = ""

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setEndereco(self, endereco):
        self.endereco = endereco
    
    def getEndereco(self):
        return self.endereco

class PessoaFisica(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.cpf = 0

    def setCpf(self, cpf):
        self.cpf = cpf
    
    def getCpf(self):
        return self.cpf

class PessoaJuridica(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.cnpj = 0
    
    def setCnpj(self, cnpj):
        self.cnpj = cnpj
    
    def getCnpj(self):
        return self.cnpj

pessoa_fisica = PessoaFisica()

pessoa_fisica.setNome("Jeziel")
print(pessoa_fisica.getNome())
pessoa_fisica.setEndereco("Rua Programação Orientada a Objetos, 90")
print(pessoa_fisica.getEndereco())
pessoa_fisica.setCpf(20240406220)
print(pessoa_fisica.getCpf())


pessoa_juridica = PessoaJuridica()

pessoa_juridica.setNome("Luiz")
print(pessoa_juridica.getNome())
pessoa_juridica.setEndereco("Rua Programação Orientada a Objetos, 92")
print(pessoa_juridica.getEndereco())
pessoa_juridica.setCnpj(60420240100064)
print(pessoa_juridica.getCnpj())