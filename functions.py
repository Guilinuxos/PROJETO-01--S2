def menu():
    menu_options = ["Acessar biblioteca", "Conferir livros alugados", "Sair"]

    while True:
        print("=== Bem-vindo à biblioteca ===")
        number = 1

        for opcao in menu_options:
            print(f"{number}. {opcao}\n")
            number += 1
        menu_question = int(input("O que você gostaria de fazer?\n\n--> "))
      
