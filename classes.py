class Livro:
    def __init__(self, titulo, autor, genero, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__ano = ano
        self.__disponivel = True

    def get_Titulo(self):
        return self.__titulo
    
    def get_Disponivel(self):
        return self.__disponivel
    
    def get_Genero(self):
        return self.__genero
    
    def get_Autor(self):
        return self.__autor
    
    def get_Ano(self):
        return self.__ano
    
    def set_Titulo(self, novotitulo):
        self.__titulo = novotitulo

    def set_Disponivel(self, status):
        self.__disponivel = status
    
    def set_Autor(self, novoautor):
        self.__autor = novoautor
    
    def set_Genero(self, novogenero):
        self.__genero = novogenero
    
    def set_Ano(self, novoano):
        self.__ano = novoano
    
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"O título {self.__titulo} foi emprestado. Redirecionando para a página inicial da biblioteca...")
        else:
            print(f"Não foi possível emprestar o título {self.__titulo}. O objeto pode ter sido obstruído ou já está sendo emprestado.")
    
    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"O título {self.__titulo} foi devolvido. Redirecionando para a página inicial da biblioteca...")
        else:
            print(f"Não foi possível devolver o título {self.__titulo}. O objeto não foi encontrado em sua lista de livros emprestados.")

# ==================== Livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899)
livro2 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance", 1881)
livro3 = Livro("Quincas Borba", "Machado de Assis", "Romance", 1891)

livro4 = Livro("Frankenstein", "Mary Shelley", "Terror", 1818)
livro5 = Livro("Drácula", "Bram Stoker", "Terror", 1897)
livro6 = Livro("Evangelho de Sangue", "Clive Barker", "Terror", 1996)

livro7 = Livro("Morangos Mofados", "Caio Fernando Abreu", "Contos", 1982)
livro8 = Livro("O Alienista", "Machado de Assis", "Contos", 1882)
livro9 = Livro("O Cartomante", "Machado de Assis", "Contos", 1884)

livro10 = Livro("Marília de Dirceu", "Tomás Antônio Gonzaga", "Poesia", 1792)
livro11 = Livro("Toda Poesia", "Paulo Leminski", "Poesia", 2013)
livro12 = Livro("Os Lusíadas", "Luís de Camões", "Poesia", 1572)
livro13 = Livro("Alguma Poesia", "Carlos Drummond de Andrade", "Poesia", 1930)

livro14 = Livro("Star Wars: Marcas da Guerra", "Chuck Wendig", "Ação", 2015)
livro15 = Livro("A Bússola de Ouro", "Philip Pullman", "Ação", 1995)
livro16 = Livro("Ponto de Impacto", "Dan Brown", "Ação", 2001)

livro17 = Livro("Apologia de Sócrates", "Platão", "Filosofia", -399) 
livro18 = Livro("O Príncipe", "Maquiavel", "Filosofia", 1532)
livro19 = Livro("A República", "Platão", "Filosofia", -380)  
livro20 = Livro("Os Dois Morrem no Final", "Adam Silvera", "Infanto Juvenil", 2017)
livro21 = Livro("Retórica", "Aristóteles", "Filosofia", -330)  
livro22 = Livro("O Diário de Anne Frank", "Anne Frank", "História", 1947)
livro23 = Livro("Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", "História", 2011)

livro24 = Livro("Diário de um Banana", "Jeff Kinney", "Infanto Juvenil", 2007)
livro25 = Livro("As Crônicas de Nárnia", "C. S. Lewis", "Infanto Juvenil", 1950)

livro26 = Livro("Pedagogia do Oprimido", "Paulo Freire", "Filosofia", 1968)
livro27 = Livro("Tópicos", "Aristóteles", "Filosofia", -350)  
livro28 = Livro("Crítica da Razão Pura", "Immanuel Kant", "Filosofia", 1781)

#-----------------------------//---------------------------------------------------

class Bibliotecário:
    def __init__(self, nome): #Atributo do objeto (nome).
        self.__nome = nome

    def ver_acervo(self, acervo): #Método para visualizar o acervo da biblioteca.
        for livro in acervo:
            print(f"Título: {livro.get_Titulo()};\nAutor: {livro.get_Autor()};\nGênero: {livro.get_Genero()};\nAno: {livro.get_Ano()};\nDisponível: {livro.get_Disponivel()}")
    def adicionar_livro(self, acervo, gênero, livro): #Método para adicionar um livro ao acervo.

        if gênero in acervo:
            acervo[gênero].append(livro)
        else:
            acervo[gênero] = [livro]
        print(f"O livro '{livro.get_Titulo()}' foi adicionado ao acervo.")

    def remover_livro(self, acervo, gênero, livro): #Método para remoção de um livro
        if gênero in acervo and livro in acervo[gênero]:
            acervo[gênero].remove(livro)
            print(f"O livro '{livro.get_Titulo()} foi removido do acervo")

    def get_nome(self):
        return self.__nome



class Visitante:
    def __init__(self, nome, CPF): #Atributo do objeto (nome).
        self.__nome = nome
        self.__CPF = CPF
        self.__livros_emprestados = []

    def ver_livros_emprestados(self):
        if not self.__livros_emprestados:
            print(f"O visitante {self.__nome} não possui livros emprestados.")
        else:
            print(f"Livros emprestados por {self.__nome}:")
            for livro in self.__livros_emprestados:
                print(f" - {livro.get_Titulo()}")
    
    def get_CPF(self):
        return self.__CPF

    def get_livros_emprestados(self):
        return self.__livros_emprestados
    
    def get_qtde_livros(self):
        return len(self.__livros_emprestados)

    def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)
        print(f"O visitante {self.__nome} emprestou o livro '{livro.get_Titulo()}'.")

    def devolver_livro(self, livro):
        if livro in self.__livros_emprestados:
            self.__livros_emprestados.remove(livro)
            print(f"O visitante {self.__nome} devolveu o livro '{livro.get_Titulo()}'.")
        else:
            print(f"O visitante {self.__nome} não possui o livro '{livro.get_Titulo()}' emprestado.")

    def reservar_livro(self, livro):
        if livro not in self.__livros_emprestados:
            self.__livros_emprestados.append(livro)
            print(f"O visitante {self.__nome} reservou o livro '{livro.get_Titulo()}'.")
        else:
            print(f"O visitante {self.__nome} já possui o livro '{livro.get_Titulo()}' emprestado.")
    
    def get_nome(self):
        return self.__nome
    
