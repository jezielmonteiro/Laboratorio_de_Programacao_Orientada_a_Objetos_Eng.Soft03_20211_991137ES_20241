#Classe Livro:

#Atributos: titulo, autor, ano_publicacao, numero_paginas, genero
#Métodos: abrir, fechar, marcar_pagina, avancar_pagina, retroceder_pagina
#• abrir(): Exibe uma mensagem indicando que o livro foi aberto.
#• fechar(): Exibe uma mensagem indicando que o livro foi fechado.
#• marcar_pagina(pagina): Marca a página atual do livro.
#• avancar_pagina(): Avança uma página, se não estiver na última página.
#• retroceder_pagina(): Retrocede uma página, se não estiver na primeira página.


class Livro:
    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.ano_publicacao = 0
        self.numero_paginas = 0
        self.genero = ""
        self.pagina_atual = 0
        self.estado = "Fechado"
    
    def setTitulo(self, titulo):
        self.titulo = titulo
    
    def getTitulo(self):
        return self.titulo
    
    def setAutor(self, autor):
        self.autor = autor
    
    def getAutor(self):
        return self.autor
    
    def setAnoPublicacao(self, ano_publicacao):
        self.ano_publicacao = ano_publicacao
    
    def getAnoPublicacao(self):
        return self.ano_publicacao
    
    def setNumeroPaginas(self, numero_paginas):
        self.numero_paginas = numero_paginas
    
    def getNumeroPaginas(self):
        return self.numero_paginas
    
    def setGenero(self, genero):
        self.genero = genero
    
    def getGenero(self):
        return self.genero
    
    def setPaginaAtual(self, pagina_atual):
        self.pagina_atual = pagina_atual
    
    def getPaginaAtual(self):
        return self.pagina_atual
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado

    def abrir(self):
        self.estado = "Aberto"
        return "Livro Aberto"
    
    def fechar(self):
        self.estado = "Fechado"
        return "Livro Fechado"

    def marcarPagina(self, pagina):
        if self.estado == "Aberto":
            self.pagina_atual = pagina

    def avancarPagina(self):
        if self.estado == "Aberto":
            if self.pagina_atual < self.numero_paginas:
                self.pagina_atual += 1

    def retrocederPagina(self):
        if self.estado == "Aberto":
            if self.pagina_atual > 1:
                self.pagina_atual -= 1
    
livro = Livro()

livro.setTitulo("Programação Orientada a Objetos")
print(livro.getTitulo())
livro.setAutor("Marco Antônio")
print(livro.getAutor())
livro.setAnoPublicacao(2024)
print(livro.getAnoPublicacao())
livro.setGenero("Obra de referência")
print(livro.getGenero())
print(livro.getEstado())
livro.abrir()
print(livro.getEstado())
livro.setNumeroPaginas(300)
print(livro.getNumeroPaginas())
livro.setPaginaAtual(1)
print(livro.getPaginaAtual())
livro.avancarPagina()
print(livro.getPaginaAtual())
livro.marcarPagina(299)
livro.avancarPagina()
print(livro.getPaginaAtual())
livro.retrocederPagina()
print(livro.getPaginaAtual())
livro.avancarPagina()
print(livro.getPaginaAtual())
livro.fechar()
print(livro.getEstado())
