#Classe Pessoa:

#Atributos: nome, idade, altura, peso
#Métodos: envelhecer, crescer, ganhar_peso, perder_peso
#• envelhecer(): Aumenta a idade da pessoa em um ano.
#• Crescer(centímetros): Aumenta a altura da pessoa em 1 centímetros, se a pessoa
#tiver menos de 21 anos.
#• Ganhar_peso(quilos): Aumenta o peso da pessoa em quilos.
#• Perder_peso(quilos): Diminui o peso da pessoa em quilos.


class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.altura = 0.0
        self.peso = 0.0
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setIdade(self, idade):
        self.idade = idade
    
    def getIdade(self):
        if self.idade > 0:
            return self.idade
    
    def setAltura(self, altura):
        self.altura = altura
    
    def getAltura(self):
        return self.altura
    
    def setPeso(self, peso):
        self.peso = peso
    
    def getPeso(self):
        return self.peso
    
    def envelhecer(self):
        self.idade += 1
    
    def crescer(self, centimetros):
        if self.idade < 21:
            self.altura += centimetros
        
    def ganharPeso(self, quilos):
        self.peso += quilos
        
    def perderPeso(self, quilos):
        self.peso -= quilos
        
pessoa = Pessoa()

pessoa.setNome("Jeziel")
print(pessoa.getNome())
pessoa.setIdade(19)
print(pessoa.getIdade())
pessoa.setAltura(180)
print(pessoa.getAltura())
pessoa.setPeso(64)
print(pessoa.getPeso())
pessoa.envelhecer()
print(pessoa.getIdade())
pessoa.crescer(5)
print(pessoa.getAltura())
pessoa.ganharPeso(6)
print(pessoa.getPeso())
pessoa.perderPeso(6)
print(pessoa.getPeso())
