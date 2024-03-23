#Classe ContaBancaria:

#Atributos: titular, numero_conta, saldo, estado
#Métodos: depositar, sacar
#•	depositar(valor): adiciona o valor ao saldo da conta.
#•	sacar(valor): subtrai o valor do saldo da conta, se houver saldo suficiente.


class ContaBancaria:
    def __init__(self):
        self.titular = ""
        self.numero_conta = 0
        self.saldo = 0.0
        self.estado ="Ativa"
    
    def setTitular(self, titular):
        self.titular = titular
    
    def getTitular(self):
        return self.titular
    
    def setNumeroConta(self, numero_conta):
        self.numero_conta = numero_conta
    
    def getNumeroConta(self):
        return self.numero_conta
    
    def setSaldo(self, saldo):
        if self.estado == "Ativa":
            if saldo >= 0:
                self.saldo = saldo
    
    def getSaldo(self):
        return self.saldo
    
    def setEstado(self, estado):
        if estado == "Ativa" or estado == "Inativa":
            self.estado = estado
    
    def getEstado(self):
        return self.estado
    
    def ativar(self):
        self.estado = "Ativa"

    def inativar(self):
        self.estado = "Inativa"

    def depositar(self, valor):
        if self.estado == "Ativa":
            if valor > 0:
                self.saldo += valor

    def sacar(self, valor):
        if self.estado == "Ativa":
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor

conta = ContaBancaria()

conta.ativar()
conta.setTitular("Jeziel")
print(conta.getTitular())
conta.setNumeroConta(20240316)
print(conta.getNumeroConta())
conta.setSaldo(1000)
print(conta.getSaldo())
conta.depositar(500)
print(conta.getSaldo())
conta.sacar(50)
print(conta.getSaldo())

