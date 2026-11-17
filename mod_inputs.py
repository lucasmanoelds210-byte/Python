import getpass

def recebe_nome(mensagem):
    while True:
        try:
            texto = getpass.getpass(mensagem)
            break
        except:
            print("Valor invalido")
    return texto


def recebe_senha(mensagem):
    while True:
        try:
            senha = getpass.getpass(input(mensagem))
            break
        except:
            print("Valor invalido!")
    return senha
