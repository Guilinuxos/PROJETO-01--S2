import os
import time
from classes import *

admin_menu_options = ["Acessar acervo", "Adicionar livros", "Remover Livros", "Alterar informações de livros", "Sair"]
visit_menu_options = ["Acessar acervo", "Conferir livros alugados", "Sair"]
lista_de_livros = [livro1, livro2, livro3, livro4, livro5, livro6, livro7, livro8, livro9, livro10, livro11, livro12, livro13, livro14, livro15, livro16, livro17, livro18, livro19, livro20, livro21, livro22]
    

# ==================== Conferir livros alugados
def check_rented():
    print("Livros alugados:")
    for livro in lista_de_livros:
        if livro.get_disponivel == False:
            print(livro)
        else:
            pass

# ==================== Alugar livro
def rent_book(visitante):

    quest = int(input("Gostaria de alugar um livro?\n1. Sim\n2. Não\n\n--> "))
    if quest == 1:
        rent_book = input("Escolha e escreva o título do livro da lista acima para alugar\n\n--> ")
        for livro in lista_de_livros:
            if livro.get_Titulo.lower() == rent_book.lower():
                visitante.emprestar_livro(livro)
                livro.emprestar()
            else:
                print("O título não foi encontrado")
    elif quest == 2:
        print("Retornando à página inicial...")
        

# ==================== Acessar biblioteca



def acervo(visitante):
    generos_livros = {
        1: "Romance",
        2: "Terror",
        3: "Contos",
        4: "Poesia",
        5: "Ação",
        6: "Filosofia",
        7: "História",
        8: "Infanto Juvenil"
    }

    
    while True:
        number = 1
        print("Acessando acervo...")
        print("Gêneros disponíveis:")
        for chave, genero in generos_livros.items():
            print(f"{chave}. {genero}")

        acervo_question = int(input("Que gênero você gostaria de acessar?\n\n--> "))
        genero_escolhido = generos_livros[acervo_question]
        print(f"=== {genero_escolhido} ===")
        for livro in lista_de_livros:
            if livro.get_Genero() == genero_escolhido:
                print(f"{number}. {livro.get_Titulo()}")
                number +=1
            else:
                pass
        rent_book(visitante)
        

# ==================== Menu Visitante
def visitor_menu(visitante):
    while True:
        number= 1
        print("=== Bem-vindo visitante ===")
        
        for opcao in visit_menu_options:
                print(f"{number}. {opcao}\n")
                number += 1
        menu_question = int(input(f"O que você gostaria de fazer?\n\n--> "))
        if menu_question == 1:
            acervo(visitante)
        elif menu_question == 2:
            pass
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
            print(f"Você entrou como {forma_login[1]}")
            login = forma_login[1]

        if login_escolhido == 1:
            pass
        elif login_escolhido == 2:
            visitor_menu(visitante)
