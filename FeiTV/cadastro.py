arquivo = "usuarios.txt"


def cadastrar():

    usuario = input("Nome de Usuário: ")
    senha = input("Senha: ")

    with open(arquivo, "r") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            if usuario == dados[0]:

                print("Este nome de usuário já existe!")
                return

    with open(arquivo, "a") as arquivo:

        arquivo.write(usuario + ";" + senha + "\n")

    print("Cadastro realizado!")


def login():

    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    with open(arquivo, "r") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            if usuario == dados[0] and senha == dados[1]:

                print("Login realizado!")
                return True

    print("Login inválido!")
    return False