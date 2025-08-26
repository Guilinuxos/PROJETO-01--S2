# ==================== Conferir livros alugados




# ==================== Acessar biblioteca




# ==================== Menu Principal

def menu():
    menu_options = ["Acessar biblioteca", "Conferir livros alugados", "Sair"]

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
