import json

# Dados
estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []


# Funções para apresentar os menus
def apresentar_menu_principal():
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao


def apresentar_menu_estudantes():
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar")
    opcao = int(input("Escolha uma opção: "))
    return opcao


# Funções para Estudantes
def salvar_estudantes(estudantes):
    with open("estudantes.json", "w") as f:
        json.dump(estudantes, f)


def carregar_estudantes():
    try:
        with open("estudantes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def incluir_estudante(estudantes):
    codigo = int(input("Digite o código do estudante: "))
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    estudantes.append(estudante)
    salvar_estudantes(estudantes)


def listar_estudantes(estudantes):
    if len(estudantes) == 0:
        print("Não há estudantes cadastrados")
    else:
        for estudante in estudantes:
            print(estudante)


def editar_estudante(estudantes):
    if len(estudantes) == 0:
        print("Não há estudantes cadastrados")
    else:
        codigo = int(input("Digite o código do estudante que deseja editar: "))
        for estudante in estudantes:
            if estudante["codigo"] == codigo:
                novo_codigo = int(input("Digite o novo código do estudante: "))
                novo_nome = input("Digite o novo nome do estudante: ")
                novo_cpf = input("Digite o novo CPF do estudante: ")
                estudante.update(
                    {"codigo": novo_codigo, "nome": novo_nome, "cpf": novo_cpf}
                )
                print("Estudante atualizado com sucesso!")
                salvar_estudantes(estudantes)
                break
        else:
            print("Estudante não encontrado")


def excluir_estudante(estudantes):
    if len(estudantes) == 0:
        print("Não há estudantes cadastrados")
    else:
        codigo = int(input("Digite o código do estudante que deseja excluir: "))
        for i, estudante in enumerate(estudantes):
            if estudante["codigo"] == codigo:
                del estudantes[i]
                print("Estudante excluído com sucesso!")
                salvar_estudantes(estudantes)
                break
        else:
            print("Estudante não encontrado")


# Funções para Professores
def salvar_professores(professores):
    with open("professores.json", "w") as f:
        json.dump(professores, f)


def carregar_professores():
    try:
        with open("professores.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def incluir_professor(professores):
    codigo = int(input("Digite o código do professor: "))
    nome = input("Digite o nome do professor: ")
    cpf = input("Digite o CPF do professor: ")
    professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
    professores.append(professor)
    salvar_professores(professores)


def listar_professores(professores):
    if len(professores) == 0:
        print("Não há professores cadastrados")
    else:
        for professor in professores:
            print(professor)


def editar_professor(professores):
    if len(professores) == 0:
        print("Não há professores cadastrados")
    else:
        codigo = int(input("Digite o código do professor que deseja editar: "))
        for professor in professores:
            if professor["codigo"] == codigo:
                novo_codigo = int(input("Digite o novo código do professor: "))
                novo_nome = input("Digite o novo nome do professor: ")
                novo_cpf = input("Digite o novo CPF do professor: ")
                professor.update(
                    {"codigo": novo_codigo, "nome": novo_nome, "cpf": novo_cpf}
                )
                print("Professor atualizado com sucesso!")
                salvar_professores(professores)
                break
        else:
            print("Professor não encontrado")


def excluir_professor(professores):
    if len(professores) == 0:
        print("Não há professores cadastrados")
    else:
        codigo = int(input("Digite o código do professor que deseja excluir: "))
        for i, professor in enumerate(professores):
            if professor["codigo"] == codigo:
                del professores[i]
                print("Professor excluído com sucesso!")
                salvar_professores(professores)
                break
        else:
            print("Professor não encontrado")


# Funções para Disciplinas
def salvar_disciplinas(disciplinas):
    with open("disciplinas.json", "w") as f:
        json.dump(disciplinas, f)


def carregar_disciplinas():
    try:
        with open("disciplinas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def incluir_disciplina(disciplinas):
    codigo = int(input("Digite o código da disciplina: "))
    nome = input("Digite o nome da disciplina: ")
    disciplina = {"codigo": codigo, "nome": nome}
    disciplinas.append(disciplina)
    salvar_disciplinas(disciplinas)


# Funções para Turmas
def salvar_turmas(turmas):
    with open("turmas.json", "w") as f:
        json.dump(turmas, f)


def carregar_turmas():
    try:
        with open("turmas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def incluir_turma(turmas):
    codigo = int(input("Digite o código da turma: "))
    codigo_professor = int(input("Digite o código do professor: "))
    codigo_disciplina = int(input("Digite o código da disciplina: "))
    turma = {
        "codigo": codigo,
        "codigo_professor": codigo_professor,
        "codigo_disciplina": codigo_disciplina,
    }
    turmas.append(turma)
    salvar_turmas(turmas)


# Funções para Matrículas
def salvar_matriculas(matriculas):
    with open("matriculas.json", "w") as f:
        json.dump(matriculas, f)


def carregar_matriculas():
    try:
        with open("matriculas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def incluir_matricula(matriculas):
    codigo_turma = int(input("Digite o código da turma: "))
    codigo_estudante = int(input("Digite o código do estudante: "))
    matricula = {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}
    matriculas.append(matricula)
    salvar_matriculas(matriculas)


# Carregar dados dos arquivos
estudantes = carregar_estudantes()
professores = carregar_professores()
disciplinas = carregar_disciplinas()
turmas = carregar_turmas()
matriculas = carregar_matriculas()

# Loop principal
while True:
    opcao = apresentar_menu_principal()
    if opcao == 1:
        while True:
            opcao = apresentar_menu_estudantes()
            if opcao == 1:
                incluir_estudante(estudantes)
            elif opcao == 2:
                listar_estudantes(estudantes)
            elif opcao == 3:
                editar_estudante(estudantes)
            elif opcao == 4:
                excluir_estudante(estudantes)
            elif opcao == 5:
                break
    elif opcao == 2:
        while True:
            opcao = apresentar_menu_professores()
            if opcao == 1:
                incluir_professor(professores)
            elif opcao == 2:
                listar_professores(professores)
            elif opcao == 3:
                editar_professor(professores)
            elif opcao == 4:
                excluir_professor(professores)
            elif opcao == 5:
                break
    elif opcao == 6:
        break
