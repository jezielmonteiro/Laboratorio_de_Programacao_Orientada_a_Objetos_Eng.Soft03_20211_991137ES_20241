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
        
        if media <= 4:
            return "Reprovado"
        if media >= 7:
            return "Aprovado"
        else:
            return "Prova Final"

aluno = Aluno()
aluno.setNome("Jeziel")
aluno.setMatricula(20240309)
aluno.setEndereco("Rua de Programação Orientada a Objetos, 90")
aluno.setTelefone("(24) 00000 - 0000")
aluno.setNota01(7)
aluno.setNota02(10)

print(aluno.getNome())
print(aluno.getMatricula())
print(aluno.getEndereco())
print(aluno.getTelefone())
print(aluno.getNota01())
print(aluno.getNota02())
print(aluno.getMedia())
