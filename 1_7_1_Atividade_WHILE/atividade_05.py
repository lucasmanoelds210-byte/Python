senha_correta = "12345"

senha = input("Digite a senha: ")

while senha != senha_correta:
    senha = input("Senha incorreta! Digite novamente: ")

print("Acesso autorizado!")