
class Livro:
    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.ano = 0
        self.editora = ""
        self.isbn = 0
        self.estado = "Disponível"
        self.emprestimos = 0
        
    def setTitulo(self, titulo):
        self.titulo = titulo
        
    def getTitulo(self):
        return self.titulo

    def setAutor(self, autor):
        self.autor = autor
    
    def getAutor(self):
        return self.autor

    def setAno(self, ano):
        self.ano = ano
    
    def getAno(self):
        return self.ano

    def setEditora(self, editora):
        self.editora = editora
    
    def getEditora(self):
        return self.editora

    def setIsbn(self, isbn):
        self.isbn = isbn
    
    def getIsbn(self):
        return self.isbn
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
    
    def setEmprestimos(self, emprestimos):
        self.emprestimos = emprestimos
    
    def getEmprestimos(self):
        return self.emprestimos

    def emprestar(self):
        if self.estado == "Disponível":
            self.emprestimos += 1
    
    def devolver(self):
        if self.estado == "Emprestado":
            return "Devolvido"
    
    def exibir(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Editora: {self.editora}, ISBN: {self.isbn}, Estado: {self.estado}, Quantidade de Empréstimos: {self.emprestimos}")
        
livro = Livro()

print(livro.getEstado())
livro.setTitulo("Programação Orientada a Objetos")
print(livro.getTitulo())
livro.setAutor("Marco Araújo")
print(livro.getAutor())
livro.setAno(5)
print(livro.getAno())
livro.setEditora("Universidade de Vassouras")
print(livro.getEditora())
livro.setIsbn(20240413)
print(livro.getIsbn())
livro.emprestar()
print(livro.getEmprestimos())
livro.setEstado("Emprestado")
print(livro.getEstado())
print(livro.devolver())
livro.exibir()


class Revista(Livro):
    def __init__(self):
        Livro.__init__(self)
        self.issn = 0
        
    def setIssn(self, issn):
        self.issn = issn
    
    def getIssn(self):
        return self.issn

    def exibir(self):
        if 0 < self.ano <= 5:
            print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Editora: {self.editora}, ISSN: {self.issn}, Estado: {self.estado}, Quantidade de Empréstimos: {self.emprestimos}")
        else:
            print("Não é possível exibir os dados da revista.")

revista = Revista()

print(revista.getEstado())
revista.setTitulo("Programação Orientada a Objetos II")
print(revista.getTitulo())
revista.setAutor("Marco Araújo")
print(revista.getAutor())
revista.setAno(10)
print(revista.getAno())
revista.setEditora("Universidade de Vassouras")
print(revista.getEditora())
revista.setIssn(13042024)
print(revista.getIssn())
revista.emprestar()
print(revista.getEmprestimos())
revista.setEstado("Emprestado")
print(revista.getEstado())
print(revista.devolver())
revista.exibir()


class Bibliotecario:
    def __init__(self):
        self.nome = ""
        self.matricula = 0
        self.telefone = 0
        self.email = ""
        self.tempo = 0
        self.salario = 0.0
        
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setMatricula(self, matricula):
        self.matricula = matricula
    
    def getMatricula(self):
        return self.matricula
    
    def setTelefone(self, telefone):
        self.telefone = telefone
    
    def getTelefone(self):
        return self.telefone
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def setTempo(self, tempo):
        self.tempo = tempo
    
    def getTempo(self):
        return self.tempo
    
    def setSalario(self, salario):
        self.salario = salario
    
    def getSalario(self):
        return self.salario
    
    def calcularSalario(self):
        self.salario = self.salario + (self.salario * (self.tempo * 0.1))
        return self.salario
    
    def exibir(self):
        print(f"Nome: {self.nome}, Matrícula: {self.matricula}, Telefone: {self.telefone}, Email: {self.email}, Tempo de Serviço (em anos): {self.tempo}, Salário: {self.salario}")
          
bibliotecario = Bibliotecario()

bibliotecario.setNome("Marco Araújo")
print(bibliotecario.getNome())
bibliotecario.setMatricula(20240413)
print(bibliotecario.getMatricula())
bibliotecario.setTelefone(2440028922)
print(bibliotecario.getTelefone())
bibliotecario.setEmail("marco.araujo@gmail.com")
print(bibliotecario.getEmail())
bibliotecario.setTempo(5)
print(bibliotecario.getTempo())
bibliotecario.setSalario(2000)
print(bibliotecario.getSalario())
print(bibliotecario.calcularSalario())
bibliotecario.exibir()


class Leitor(Bibliotecario):
    def __init__(self):
        Bibliotecario.__init__(self)
        self.endereco = ""
        self.idade = 0
    
    def setEndereco(self, endereco):
        self.endereco = endereco
    
    def getEndereco(self):
        return self.endereco

    def setIdade(self, idade):
        self.idade = idade
    
    def getIdade(self):
        return self.idade

    def validar(self):
        if self.idade < 18:
            return "O leitor não pode fazer empréstimos de livros."
        else:
            return "Empréstimos liberados!"
    
    def incrementarIdade(self, ano):
        if ano > 0:
            self.idade += ano
    
    def diminuirIdade(self, ano):
        if ano > 0:
            if ano < self.idade:
                self.idade -= ano
    
    def exibir(self):
        print(f"Nome: {self.nome}, Endereço: {self.endereco}, Telefone: {self.telefone}, Email: {self.email}, Idade: {self.idade}")
            
leitor = Leitor()

leitor.setNome("Jeziel")
print(leitor.getNome())
leitor.setEndereco("Logradouro: Jardim Bonito, Número: 13, Complemento: Perto do Mercado São João, Bairro: Jardim Bonito, Cidade: Valença, Estado: Rio de Janeiro, CEP: 13400-000")
print(leitor.getEndereco())
leitor.setTelefone(2420241304)
print(leitor.getTelefone())
leitor.setEmail("jeziel@gmail.com")
print(leitor.getEmail())
leitor.setIdade(20)
print(leitor.getIdade())
print(leitor.validar())
leitor.incrementarIdade(2)
print(leitor.getIdade())
leitor.diminuirIdade(2)
print(leitor.getIdade())
leitor.exibir()
