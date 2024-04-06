#Classes: Aluno, Aluno Graduacao, Aluno Pos Graduacao

#Aluno: nome, matricula, nota 1, nota 2, método para calcular média
#Aluno Graduacao: método para verificar aprovação (média >= 6)
#Aluno Pós Graduacao: método para verificar aprovação (média >= 7)


class Aluno():
    def __init__(self):
        self.nome = ""
        self.matricula = 0
        self.nota1 = 0.0
        self.nota2 = 0.0
        self.media = 0.0
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setMatricula(self, matricula):
        self.matricula = matricula
        
    def getMatricula(self):
        return self.matricula
    
    def setNota1(self, nota1):
        self.nota1 = nota1
    
    def getNota1(self):
        return self.nota1
    
    def setNota2(self, nota2):
        self.nota2 = nota2

    def getNota2(self):
        return self.nota2
    
    def getMedia(self):
        media = (self.nota1 + self.nota2) / 2
        return media

class AlunoGraduacao(Aluno):
    def __init__(self):
        Aluno.__init__(self) 
    
    def verificarAprovacao(self):
        if self.getMedia() >= 6:
            return "Aluno Aprovado!"
        else:
            return "Aluno Reprovado!"

class AlunoPosGraduacao(Aluno):
    def __init__(self):
        Aluno.__init__(self)

    def verificarAprovacao(self):
        if self.getMedia() >= 7:
            return "Aluno Aprovado!"
        else:
            return "Aluno Reprovado!"

aluno_graduacao = AlunoGraduacao()

aluno_graduacao.setNome("Jeziel")
print(aluno_graduacao.getNome())
aluno_graduacao.setMatricula(20240406)
print(aluno_graduacao.getMatricula())
aluno_graduacao.setNota1(8)
print(aluno_graduacao.getNota1())
aluno_graduacao.setNota2(7.2)
print(aluno_graduacao.getNota2())
print(aluno_graduacao.getMedia())
aluno_graduacao.verificarAprovacao()
print(aluno_graduacao.verificarAprovacao())


aluno_posgraduacao = AlunoPosGraduacao()

aluno_posgraduacao.setNome("Luiz")
print(aluno_posgraduacao.getNome())
aluno_posgraduacao.setMatricula(60042024)
print(aluno_posgraduacao.getMatricula())
aluno_posgraduacao.setNota1(9)
print(aluno_posgraduacao.getNota1())
aluno_posgraduacao.setNota2(7.5)
print(aluno_posgraduacao.getNota2())
print(aluno_posgraduacao.getMedia())
print(aluno_posgraduacao.verificarAprovacao())