class Aluno:
    def __init__(self):
        self.nome = ""
        self.matricula = 0
        self.endereco = ""
        self.telefone = ""
        self.nota1 = 0
        self.nota2 = 0
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setMatricula(self, matricula):
        self.matricula = matricula
    
    def getMatricula(self):
        return self.matricula
    
    def setEndereco(self, endereco):
        self.endereco = endereco
    
    def getEndereco(self):
        return self.endereco
    
    def setTelefone(self, telefone):
        self.telefone = telefone
    
    def getTelefone(self):
        return self.telefone
    
    def setNota01(self, nota01):
        self.nota01 = nota01
    
    def getNota01(self):
        return self.nota01
    
    def setNota02(self, nota02):
        self.nota02 = nota02

    def getNota02(self):
        return self.nota02
    
    def getMedia(self):
        media = (self.nota01 + self.nota02) / 2
        return media
        
    def getSituacao(self):
        if self.getMedia() <= 4:
            situacao = "Reprovado"
        if self.getMedia() >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Prova Final"
        return situacao

aluno = Aluno()
aluno.setNome("Jeziel")
print(aluno.getNome())
aluno.setMatricula(20240309)
print(aluno.getMatricula())
aluno.setEndereco("Rua de Programação Orientada a Objetos, 90")
print(aluno.getEndereco())
aluno.setTelefone("(24) 00000 - 0000")
print(aluno.getTelefone())
aluno.setNota01(7)
print(aluno.getNota01())
aluno.setNota02(10)
print(aluno.getNota02())
