estudantes = []

def menu_principal():
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def menu_estudantes():
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar")
    opcao = int(input("Escolha uma opção: "))
    return opcao

while True:
    opcao = menu_principal()
    if opcao == 1:
        while True:
            opcao = menu_estudantes()
            if opcao == 1:
                nome = input("Digite o nome do estudante: ")
                estudantes.append(nome)
            elif opcao == 2:
                if len(estudantes) == 0:
                    print("Não há estudantes cadastrados")
                else:
                    for estudante in estudantes:
                        print(estudante)
            elif opcao in [3, 4]:
                print("EM DESENVOLVIMENTO")
            elif opcao == 5:
                break
    elif opcao in [2, 3, 4, 5]:
        print("EM DESENVOLVIMENTO")
    elif opcao == 6:
        break
