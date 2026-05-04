SENHA_CORRETA = "python12345"

while True:
    senha = input("Digite a senha: ")
    if senha == SENHA_CORRETA:
        print("Acesso permitido!")
        break
    print("Senha incorreta! Tente novamente.")