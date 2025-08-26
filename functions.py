import os
import time
from classes import *

# ==================== Conferir livros alugados




# ==================== Acessar biblioteca

def acervo():
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


    lista_de_livros = [livro1, livro2, livro3, livro4, livro5, livro6, livro7, livro8, livro9, livro10, livro11, livro12, livro13, livro14, livro15, livro16, livro17, livro18, livro19, livro20, livro21, livro22]
    
    while True:
        number = 1
        print("=== Bem vindo à biblioteca ===")
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


# ==================== Menu Principal

def menu():
    menu_options = ["Acessar acervo", "Conferir livros alugados", "Sair"]

    while True:
        print("=== Bem-vindo à biblioteca ===")
        number = 1

        for opcao in menu_options:
            print(f"{number}. {opcao}\n")
            number += 1
        menu_question = int(input("O que você gostaria de fazer?\n\n--> "))

        if menu_question > 3 or menu_question < 1:
            while menu_question > 3 or menu_question < 1:
                print("Escolha uma opção disponível")
                menu_question = int(input("--> "))
        elif menu_question == 1:
            pass
        elif menu_question == 2:
            pass
        elif menu_question == 3:
            print("Saindo...")
            os.system("pause")
            os.system("cls")
            break
