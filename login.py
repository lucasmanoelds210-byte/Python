import mod_msg
import mod_inputs

USUARIO = "lucas"
SENHA = "12345"

def valida_usuario(user):
    while True:
        usuario = mod_inputs.recebe_nome("Digite seu usuario: ")

        if len(usuario) >=5:
            if user == usuario:
                    break
            else:
                    print("Senha ")
        else:
            print("A senha deve conter 5 Digitos")

    return usuario

def valida_senha(senha1):
    while True:
        senha = mod_inputs.recebe_senha("Digite sua senha: ")
        if senha == senha1: 
            break
        else:
            print("Senha invalida\n")
    return senha

def main():
    mod_msg.msg_login_ini()
    userValido = valida_usuario(USUARIO)
    senha_validada = valida_senha(SENHA)
    print("Sucesso! O usuario e:", USUARIO)

    