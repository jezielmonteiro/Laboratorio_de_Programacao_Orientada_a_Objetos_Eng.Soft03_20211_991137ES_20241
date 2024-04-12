#Classe Funcionario:

#Atributos: nome, cargo, salario, departamento
#Métodos: receber_aumento, mudar_departamento, exibir_dados
#• receber_aumento(percentual): Aplica um aumento de percentual ao salario.
#• mudar_departamento(novo_departamento): Altera o departamento para o
#novo_departamento.
#• exibir_dados(): Exibe os dados do funcionário, incluindo nome, cargo, salário e
#departamento.


class Funcionario:
    def __init__(self):
        self.nome = ""
        self.cargo = ""
        self.salario = 0.0
        self.departamento = ""

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setCargo(self, cargo):
        self.cargo = cargo
    
    def getCargo(self):
        return self.cargo

    def setSalario(self, salario):
        self.salario = salario
    
    def getSalario(self):
        return self.salario
    
    def setDepartamento(self, departamento):
        self.departamento = departamento
    
    def getDepartamento(self):
        return self.departamento
    
    def receberAumento(self, percentual):
        if percentual > 0:
            self.salario = self.salario + (self.salario * (percentual / 100))

    def mudarDepartamento(self, novo_departamento):
        self.departamento = novo_departamento
    
    def exibirDados(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario}, Departamento: {self.departamento}")
    
funcionario = Funcionario()

funcionario.setNome("Pedrodbr")
print(funcionario.getNome())
funcionario.setCargo("Streamer")
print(funcionario.getCargo())
funcionario.setSalario(500)
print(funcionario.getSalario())
funcionario.setDepartamento("Twitch")
print(funcionario.getDepartamento())
funcionario.receberAumento(50)
funcionario.mudarDepartamento("Cock Department")
funcionario.exibirDados()
