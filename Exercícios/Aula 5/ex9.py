#Classes: Funcionário, Gerente, Diretor

#Funcionário: nome, cpf, salário, método para calcular bônus (5% do salário)
#Gerente: departamento, método para calcular bônus (10% do salário + 500)
#Diretor: método para calcular bônus (15% do salário + 1000)


class Funcionario:
    def __init__(self):
        self.nome = ""
        self.cpf = 0.0
        self.salario = 0.0

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf
    
    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario
    
    def getBonus(self):
        bonus = self.salario * 5/100
        return bonus
    
class Gerente(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)
        self.departamento = ""
    
    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento

    def getBonus(self):
        bonus = (self.salario * 10 / 100) + 500
        return bonus

class Diretor(Funcionario):
    def __init__(self):
        Funcionario.__init__(self)

    def getBonus(self):
        bonus = (self.salario * 15 / 100) + 1000
        return bonus
    
funcionario = Funcionario()

funcionario.setNome("Monteiro")
print(funcionario.getNome())
funcionario.setCpf(20240412202)
print(funcionario.getCpf())
funcionario.setSalario(2000)
print(funcionario.getSalario())
print(funcionario.getBonus())


gerente = Gerente()

gerente.setNome("Luiz")
print(gerente.getNome())
gerente.setCpf(12042024120)
print(gerente.getCpf())
gerente.setSalario(5000)
print(gerente.getSalario())
gerente.setDepartamento("Cock Department")
print(gerente.getDepartamento())
print(gerente.getBonus())


diretor = Diretor()

diretor.setNome("Jeziel")
print(diretor.getNome())
diretor.setCpf(41220244122)
print(diretor.getCpf())
diretor.setSalario(8000)
print(diretor.getSalario())
print(diretor.getBonus())
