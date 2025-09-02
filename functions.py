import os
from classes import *

admin_menu_options = ["Acessar acervo", "Adicionar livros", "Remover Livros", "Alterar informações de livros", "Sair"]
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
def check_rented():
    while True:
        rented_books = []
        counter = 0
        number = 1
        for livro in acervo:
            if not livro.get_Disponivel():
                rented_books.append(livro)
                counter+=1
        if not rented_books:
            print("Nenhum livro foi alugado até o momento.")
        else:
            for livro in rented_books:
                print(f"{number}. {livro.get_Titulo()}")
                number+=1
        break
        

# ==================== Alugar livro
def rent_book(visitante):
    while True:
        found_book = False
        quest = int(input("Gostaria de alugar um livro?\n1. Sim\n2. Não\n\n--> "))
        if quest == 1:
            rent_book = input("Escolha e escreva o título do livro da lista acima para alugar\n\n--> ")

            for livro in acervo:
                if rent_book.lower() == livro.get_Titulo().lower():
                    found_book = True

                    if livro.get_Disponivel():
                        visitante.emprestar_livro(livro)
                        livro.emprestar()
                        break
                    else:
                        print("O livro já está sendo alugado")
                    break

            if found_book == False:
                print("O livro já está sendo alugado ou não existe")    

        elif quest == 2:
            print("Retornando à página inicial...")
            break
        

# ==================== Acessar biblioteca



def showacervo(visitante = None):
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
            # só mostra o que sua classe Livro já suporta
            print(f"- {livro.get_Titulo()} | {livro.get_Autor()} | {livro.get_Ano()} | {status}")

        print()
    if visitante:
        rent_book(visitante)

    
    while True:
        number = 1
        print("Acessando acervo...")
        showacervo()

        acervo_question = int(input("Que gênero você gostaria de acessar?\n\n--> "))
        genero_escolhido = acervo[acervo_question]
        print(f"=== {genero_escolhido} ===")
        for livro in acervo:
            if livro.get_Genero() == genero_escolhido:
                print(f"{number}. {livro.get_Titulo()}")
                number +=1
            else:
                pass
        rent_book(visitante)
        break
        


# ==================== Menu Bibliotecário
def bible_menu():
    while True:
        number = 1
        print("=== Bem-vindo bibliotecário ===")

        for opcao in admin_menu_options:
            print(f"{number}. {opcao}\n")
            number+=1

        menu_question = int(input("O que você gostaria de fazer?\n\n--> "))
        if menu_question == 1:
            pass
        elif menu_question == 2:
            pass
        elif menu_question == 3:
            pass
        elif menu_question == 4:
            pass
        elif menu_question == 5:
            print("Saindo...")
            break






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
            visitante.devolver_livro()

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
            pass
        elif login_escolhido == 2:
            visitor_menu(visitante)
