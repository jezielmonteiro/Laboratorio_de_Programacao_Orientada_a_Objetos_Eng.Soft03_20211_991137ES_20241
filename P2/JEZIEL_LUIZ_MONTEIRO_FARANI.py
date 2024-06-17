class Escolaridade():
    def __init__(self):
        self.nome = ""
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

class Funcionario():
    def __init__(self):
        self.escolaridade = None
        self.pais = None
        self.estado = None
        self.filial = None
        
    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    
    def getEscolaridade(self):
        return self.escolaridade
    
    def setPais(self, pais):
        self.pais = pais
    
    def getPais(self):
        return self.pais
    
    def getNomePais(self):
        if self.pais == None:
            return "Funcionário sem país de alocação"
        else:
            return self.pais.getNome()
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
    
    def getNomeEstado(self):
        if self.estado == None:
            return "Funcionário sem estado de filial"
        else:
            return self.estado.getNome()
        
    def setFilial(self, filial):
        self.filial = filial
    
    def getFilial(self):
        return self.filial
        
class Grupo():
    def __init__(self):
        self.presidente = None
        self.escolaridade = None
        
    def setPresidente(self, presidente):
        self.presidente = presidente
    
    def getPresidente(self):
        return self.presidente
    
    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade
        
    def getEscolaridade(self, escolaridade):
        return self.escolaridade
    
    def getNomeEscolaridade(self):
        if self.escolaridade == None:
            return "Presidente sem escolaridade"
        else:
            return self.escolaridade.getNome()

class Pais():
    def __init__(self):
        self.nome = None
        self.sede = None
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

    def setSede(self, sede):
        self.sede = sede
    
    def getSede(self):
        return self.sede
    
class Estado():
    def __init__(self):
        self.nome = None
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

class Filial():
    def __init__(self):
        self.estado = None
        self.empresa = None
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
    
    def getNomeEstadoFilial(self):
        if self.estado == None:
            return "Filial sem estado"
        else:
            return self.estado.getNome()
    
    def setEmpresa(self, empresa):
        self.empresa = empresa
    
    def getEmpresa(self):
        return self.empresa
    
    def getNomeDiretorEmpresa(self):
        if self.empresa == None:
            return "Diretor sem empresa"
        else:
            return self.empresa.getDiretor()
        
class Departamento():
    def __init__(self):
        self.chefia = None
        self.escolaridade = None
    
    def setChefia(self, chefia):
        self.chefia = chefia
    
    def getChefia(self):
        return self.chefia

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade
    
    def getEscolaridade(self):
        return self.escolaridade
    
    def getNomeEscolaridade(self):
        if self.chefia == None:
            return "Departamento sem chefia"
        else:
            return self.escolaridade.getNome()

class Empresa():
    def __init__(self):
        self.diretor = None
    
    def setDiretor(self, diretor):
        self.diretor = diretor
    
    def getDiretor(self):
        return self.diretor

#(1)
escolaridade = Escolaridade()
escolaridade.setNome("Doutorado")

grupo = Grupo()
grupo.setPresidente("Presidente 1")
grupo.setEscolaridade(escolaridade)
print(grupo.getNomeEscolaridade())

#(2)
pais = Pais()
pais.setNome("Brasil")

funcionario = Funcionario()
funcionario.setPais(pais)
print(funcionario.getNomePais())

#(3)
estado = Estado()
estado.setNome("Rio de Janeiro")

filial = Filial()
filial.setEstado(estado)
print(filial.getNomeEstadoFilial())

#(4)
escolaridade1 = Escolaridade()
escolaridade1.setNome("Mestrado")

departamento = Departamento()
departamento.setChefia("Chefia 1")
departamento.setEscolaridade(escolaridade1)
print(departamento.getNomeEscolaridade())

#(5)
empresa = Empresa()
empresa.setDiretor("Diretor 1")

filial1 = Filial()
filial1.setEmpresa(empresa)
print(filial1.getNomeDiretorEmpresa())