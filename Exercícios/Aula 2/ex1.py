#Classe Carro:

#Atributos: marca, modelo, ano, cor, velocidade_atual
#Métodos: acelerar, frear, ligar, desligar
#•	acelerar(quantidade): aumenta a velocidade atual do carro pela quantidade especificada.
#•	frear(quantidade): diminui a velocidade atual do carro pela quantidade especificada, sem deixar que a velocidade fique negativa.
#•	ligar(): altera o estado do carro para ligado.
#•	desligar(): altera o estado do carro para desligado e zera a velocidade atual.


class Carro:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.ano = 0
        self.cor = ""
        self.velocidade = 0
        self.estado = "Desligado"
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def setAno(self, ano):
        self.ano = ano
    
    def getAno(self):
        return self.ano
    
    def setCor(self, cor):
        self.cor = cor
    
    def getCor(self):
        return self.cor
    
    def setVelocidade(self, velocidade):
        if self.estado == "Ligado":
            if velocidade >= 0:
                self.velocidade = velocidade
    
    def getVelocidade(self):
        return self.velocidade
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
    
    def ligar(self):
        self.estado = "Ligado"
    
    def desligar(self):
        self.estado = "Desligado"
        self.velocidade = 0

    def acelerar(self, quantidade):
        if self.estado == "Ligado":
            self.velocidade += quantidade

    def frear(self, quantidade):
        if self.estado == "Ligado":
            self.velocidade -= quantidade
            if self.velocidade < 0:
                self.velocidade = 0

carro = Carro()

carro.setMarca("Nissan")
print(carro.getMarca())
carro.setModelo("180SX")
print(carro.getModelo())
carro.setAno(1988)
print(carro.getAno())
carro.setCor("Vermelho")
print(carro.getCor())
print(carro.getEstado())
print(carro.getVelocidade())
carro.ligar()
print(carro.getEstado())
carro.setVelocidade(190)
print(carro.getVelocidade())
carro.acelerar(30)
print(carro.getVelocidade())
carro.frear(20)
print(carro.getVelocidade())
carro.desligar()
print(carro.getEstado())
print(carro.getVelocidade())
