class Pessoa():
    def __init__(self):
        self.nome = ""
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)

class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)

class Turma():
    def __init__(self):
        self.turma = ""
        self.alunos = []
    
    def setNome(self, turma):
        self.turma = turma

    def getNome(self):
        return self.turma

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def exibirNomesAlunos(self):
        for aluno in self.alunos:
            print(aluno.getNome())

    def verificarAluno(self, aluno):
        return aluno in self.alunos

    def excluirAluno(self, aluno):
        self.alunos.remove(aluno)

class Curso():
    def __init__(self):
        self.professores = [] 
        self.disciplinas = []
        self.alunos = []
        self.turmas = []

    def ingressar(self, professor):
        self.professores.append(professor)
    
    def exibirNomesProfessores(self):
        for professor in self.professores:
            print(professor.getNome())
    
    def matricular(self, aluno):
        self.alunos.append(aluno)

    def exibirNomesAlunos(self):
        for aluno in self.alunos:
            print(aluno.getNome())
    
    def verificarAluno(self, aluno):
        return aluno in self.alunos
    
    def excluirAluno(self, aluno):
        self.alunos.remove(aluno)
    
    def incluirDisciplina(self, disciplina):
        self.disciplinas.append(disciplina)
    
    def exibirDisciplinas(self):
        for disciplina in self.disciplinas:
            print(disciplina.getNome())
    
    def criarTurma(self, turma):
        self.turmas.append(turma)
    
    def exibirTurmas(self):
        for turma in self.turmas:
            print(turma.getNome())

    def verificarTurma(self, turma):
        return turma in self.turmas
    
    def excluirTurma(self, turma):
        self.turmas.remove(turma)

class Disciplina():
    def __init__(self):
        self.disciplina = ""
    
    def setNome(self, disciplina):
        self.disciplina = disciplina
    
    def getNome(self):
        return self.disciplina

#(1)
professor1 = Professor()
professor1.setNome("Marco Antônio")
print(professor1.getNome())

#(2)
turma = Turma()

aluno1 = Aluno()
aluno1.setNome("João")
aluno2 = Aluno()
aluno2.setNome("Maria")
aluno3 = Aluno()
aluno3.setNome("Ana")

turma.matricular(aluno1)
turma.matricular(aluno2)
turma.exibirNomesAlunos()

#(3)
curso = Curso()

professor1 = Professor()
professor1.setNome("Marco Antônio")
professor2 = Professor()
professor2.setNome("Caio Jannuzzi")
professor3 = Professor()
professor3.setNome("Tássio Auad")
curso.ingressar(professor1)
curso.ingressar(professor2)
curso.ingressar(professor3)
curso.exibirNomesProfessores()

#(4)
turma1 = Turma()

aluno1 = Aluno()
aluno1.setNome("Jeziel")
aluno2 = Aluno()
aluno2.setNome("Luiz")
aluno3 = Aluno()
aluno3.setNome("Felipe")
curso.matricular(aluno1)
curso.matricular(aluno2)
curso.matricular(aluno3)
curso.exibirNomesAlunos()

#(5)
curso1 = Curso()

aluno1 = Aluno()
aluno1.setNome("Pedro")
aluno2 = Aluno()
aluno2.setNome("Higor")
aluno3 = Aluno()
aluno3.setNome("Leonardo")
curso1.matricular(aluno1)
curso1.matricular(aluno2)
curso1.matricular(aluno3)
curso1.exibirNomesAlunos()

#(6)
turma2 = Turma()

disciplina1 = Disciplina()
disciplina1.setNome("Laboratório de Programação Orientada a Objetos")
disciplina2 = Disciplina()
disciplina2.setNome("Estrutura de Dados")
disciplina3 = Disciplina()
disciplina3.setNome("Laboratório de Programação FrontEnd")
curso.incluirDisciplina(disciplina1)
curso.incluirDisciplina(disciplina2)
curso.incluirDisciplina(disciplina3)
curso.exibirDisciplinas()

#(7)
turma3 = Turma()

aluno1 = Aluno()
aluno1.setNome("Izabel")
aluno2 = Aluno()
aluno2.setNome("Lívia")
aluno3 = Aluno()
aluno3.setNome("Luiz")
turma3.matricular(aluno1)
turma3.matricular(aluno2)
print(turma3.verificarAluno(aluno1))
print(turma3.verificarAluno(aluno2))
print(turma3.verificarAluno(aluno3))

#(8)
curso2 = Curso()

aluno1 = Aluno()
aluno1.setNome("Kauã")
aluno2 = Aluno()
aluno2.setNome("Cleiton")
aluno3 = Aluno()
aluno3.setNome("Vicente")
curso2.matricular(aluno2)
print(curso2.verificarAluno(aluno1))
print(curso2.verificarAluno(aluno2))
print(curso2.verificarAluno(aluno3))

#(9)
curso3 = Curso()

turma4 = Turma()
curso3.criarTurma(turma4)
turma5 = Turma()
curso3.criarTurma(turma5)
turma6 = Turma()
print(curso3.verificarTurma(turma4))
print(curso3.verificarTurma(turma5))
print(curso3.verificarTurma(turma6))

#(10)
turma7 = Turma()

aluno1 = Aluno()
aluno1.setNome("Deividy")
aluno2 = Aluno()
aluno2.setNome("Kayke")
aluno3 = Aluno()
aluno3.setNome("Thiago")
turma7.matricular(aluno1)
turma7.matricular(aluno2)
turma7.matricular(aluno3)
turma7.excluirAluno(aluno2)
turma7.exibirNomesAlunos()

#(11)
curso4 = Curso()

turma8 = Turma()
turma8.setNome("Turma 8")
curso4.criarTurma(turma8)
turma9 = Turma()
turma9.setNome("Turma 9")
curso4.criarTurma(turma9)
turma10 = Turma()
turma10.setNome("Turma 10")
curso4.criarTurma(turma10)
curso4.excluirTurma(turma9)
curso4.exibirTurmas()

#(12)
curso5 = Curso()

aluno1 = Aluno()
aluno1.setNome("Felipe")
aluno2 = Aluno()
aluno2.setNome("Luiz")
aluno3 = Aluno()
aluno3.setNome("Julio")
curso5.matricular(aluno1)
curso5.matricular(aluno2)
curso5.matricular(aluno3)
curso5.excluirAluno(aluno2)
curso5.exibirNomesAlunos()
