import os
from classes import *

admin_menu_options = ["Acessar acervo", "Adicionar livros", "Remover Livros", "Alterar informações de livros", "Ver livros alugados", "Sair"]
visit_menu_options = ["Acessar acervo", "Conferir livros alugados", "Sair"]
acervo = {
    "Romance": [livro1, livro2, livro3],
    "Terror": [livro4, livro5, livro6],
    "Contos": [livro7, livro8, livro9],
    "Poesia": [livro10, livro11, livro13],
    "Ação": [livro14, livro15, livro16],
    "Filosofia": [livro17, livro18, livro19, livro20, livro21, livro26, livro27, livro28],
    "História": [livro22, livro23],
    "Infanto Juvenil": [livro24, livro25]
}
# ==================== Conferir livros alugados
def check_rented(visitante = None):
    if visitante:
        visitante.ver_livros_emprestados()
    else:
        rented_books = []
        number = 1

        print("Todos os livros alugados\n")

        for genero in acervo.values():
            for livro in genero:
                if not livro.get_Disponivel():
                    rented_books.append(livro)

        if not rented_books:
            print("Nenhum livro foi alugado até o momento")
        else:
            for livro in rented_books:
                print(f"{number}: {livro.get_Titulo()}")
                number += 1

        

# ==================== Alugar livro
def rent_book(visitante):

    if visitante.get_qtde_livros() >= 2:
        print("Você já atingiu o limite de 2 livros")
        print("Devolva um livro para pegar outro")
        return
    
    while True:
        found_book = False
        quest = int(input("Gostaria de alugar um livro?\n1. Sim\n2. Não\n\n--> "))
        if quest == 1:
            rent_book_title = input("Escolha e escreva o título do livro da lista acima para alugar\n\n--> ")

            for genero in acervo.values():
                for livro in genero:
                    if rent_book_title.lower() == livro.get_Titulo() .lower():
                        found_book = True
                        if livro.get_Disponivel():
                            visitante.emprestar_livro(livro)
                            livro.emprestar()
                            return
                        break
            if not found_book:
                print("Livro não encontrado")    

        elif quest == 2:
            print("Retornando à página inicial...")
            break
        

# ==================== Acessar biblioteca



def showacervo(visitante=None):

    if visitante:
        print(f"Seus livros alugados: {visitante.get_qtde_livros()})")

    print("Acervo da biblioteca:\n")
    for genero, livros in acervo.items():
        print(f"== {genero} ==")
        if not livros:
            print("Nenhum livro cadastrado")
        for livro in livros:
            if livro.get_Disponivel():
                status = "Disponível"
            else:
                status = "Indisponível"
            print(f"- {livro.get_Titulo()} | {livro.get_Autor()} | {livro.get_Ano()} | {status}")
        print()
    
    if visitante:
        rent_book(visitante)
        


# ==================== Menu Bibliotecário
def bible_menu():
    while True:
        number = 1
        print("=== Bem-vindo bibliotecário ===")

        for opcao in admin_menu_options:
            print(f"{number}. {opcao}")
            number += 1

        menu_question = int(input("\nO que você gostaria de fazer?\n\n--> "))
        
        if menu_question == 1:
            showacervo()  # Acessar acervo
            
        elif menu_question == 2:
            add_livro()  # Adicionar livros
            
        elif menu_question == 3:
            remover_livro()  # Remover Livros
            
        elif menu_question == 4:
            alterar_livro()  # Alterar informações de livros
            
        elif menu_question == 5:
            book_book()  # Ver livros alugados
            
        elif menu_question == 6: #sair
            print("Saindo...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")
# ==================== Add Livro
def add_livro():                      
    print("Adicionar novo livro")
    titulo = input("Título:")
    autor = input("Autor:")
    genero = input("Gênero:")
    ano = int(input("Ano:"))

    novo_livro = Livro(titulo, autor, genero, ano)

    if genero in acervo:
        acervo[genero].append(novo_livro)
    else:
        acervo[genero] = [novo_livro]

    print(f"Livro '{titulo}' adicionado ao acervo")

# ==================== Remover Livro
def remover_livro():
    print("Remover Livro")
    titulo = input("Digite o título do livro a ser removido:")

    for genero, livros in acervo.items():
        for livro in livros:
            if livro.get_Titulo().lower() == titulo.lower():
                livros.remove(livro)
                print(f"Livro '{titulo}' removido")
                return
    print("Livro não encontrado")
# ==================== Alterar Livro
def alterar_livro():    
    print("Alterar informações do livro")
    titulo = input("Digite o título do livro a ser alterado:")

    livro_encontrado = None
    genero_original = None
    for genero, livros in acervo.items():
        for livro in livros:
            if livro.get_Titulo().lower() == titulo.lower():
                livro_encontrado = livro
                genero_original = genero
                break
        if livro_encontrado:
            break

    if not livro_encontrado:
        print("Livro não encontrado")
        return

    print("Deixe em branco, assim mantém o valor atual:")

    novotitulo = input(f"Novo título [{livro_encontrado.get_Titulo()}]:") or livro_encontrado.get_Titulo()
    novoautor = input(f"Novo autor [{livro_encontrado.get_Autor()}]:") or livro_encontrado.get_Autor()
    novogenero = input(f"Novo gênero [{livro_encontrado.get_Genero()}]:") or livro_encontrado.get_Genero()
    novoano = input(f"Novo ano [{livro_encontrado.get_Ano()}]:") or livro_encontrado.get_Ano()

    if novogenero != genero_original:
    
        acervo[genero_original].remove(livro_encontrado)
        
        if novogenero in acervo:
            acervo[novogenero].append(livro_encontrado)
        else:
            acervo[novogenero] = [livro_encontrado]

    livro_encontrado.set_Titulo(novotitulo)
    livro_encontrado.set_Autor(novoautor)
    livro_encontrado.set_Genero(novogenero)
    if novoano:
        livro_encontrado.set_Ano(int(novoano))
    else:
        livro_encontrado.set_Ano(livro_encontrado.get_Ano())
    
    print("Livro atualizado com sucesso!")
# ==================== VER TODOS ALUGADOS
def book_book():
    print("Ver todos os livros alugados")
    alugados = []

    for genero, livros in acervo.items():
        for livro in livros:
            if not livro.get_Disponivel():
                alugados.append(livro)

    if not alugados:
        print("Nenhum livro foi alugado no momento")
    else:
        number = 1
        for livro in alugados:
            print(f"{number}: {livro.get_Titulo()} - {livro.get_Genero()}")
            number += 1



# ==================== Devolução
def devolver_livro_menu(visitante):
    if visitante.get_qtde_livros() == 0:
        print("Você não tem livros para devolver.")
        return
    
    print("=== SEUS LIVROS ALUGADOS ===")
    print(f"Livros alugados: {visitante.get_qtde_livros()}/2")
    
    livros = visitante.get_livros_emprestados()
    for i in range(len(livros)):
        livro = livros[i]
        print(f"{i+1}. {livro.get_Titulo()}")
    
    escolha = input("\nEscolha o número do livro para devolver: ")
    
    if escolha == "1" and len(livros) >= 1:
        livro = livros[0]
        visitante.devolver_livro(livro)  # ← Aqui sim passa um livro
        livro.devolver()
    elif escolha == "2" and len(livros) >= 2:
        livro = livros[1]
        visitante.devolver_livro(livro)  # ← Aqui sim passa um livro
        livro.devolver()
    else:
        print("Número inválido.")


# ==================== Menu Visitante
def visitor_menu(visitante: Visitante):
    while True:
        number= 1
        print("=== Bem-vindo visitante ===")
        
        for opcao in visit_menu_options:
                print(f"{number}. {opcao}\n")
                number += 1
        menu_question = int(input(f"O que você gostaria de fazer?\n\n--> "))
        if menu_question == 1:
            showacervo(visitante)
            
        elif menu_question == 2:
            devolver_livro_menu(visitante)  # ← FUNÇÃO, não método da classe
            
        elif menu_question == 3:
            print("Voltando à tela inicial")
            break
        









# ==================== Cadastrando a pessoa

def cadastro():
    nome = input("Qual seu nome?\n\n--> ")
    visitante = Visitante(nome)
    return visitante
    

# ==================== Menu Principal

def menu():
    forma_login = ["Bibliotecario", "Visitante"]
    visitante = cadastro()

    while True:
        print("=== Bem-vindo à biblioteca ===")

        number = 1

        for login in forma_login:
            print(f"{number}. {login}")
            number+=1

        login_escolhido = int(input("Como você gostaria de entrar?\n\n--> "))
        if login_escolhido == 1:
            print(f"Você entrou como {forma_login[0]}")
            login = forma_login[0]
        elif login_escolhido == 2:
            visitor_menu(visitante)
            print(f"Você entrou como {forma_login[1]}")
            login = forma_login[1]

        if login_escolhido == 1:
            bible_menu()
        elif login_escolhido == 2:
            visitor_menu(visitante)
