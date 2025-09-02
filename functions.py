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
            pass
        elif login_escolhido == 2:
            visitor_menu(visitante)
