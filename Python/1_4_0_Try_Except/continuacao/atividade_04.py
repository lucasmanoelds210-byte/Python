try:
    nome = (input("Digite seu nome completo"))
    print("o nome do usuario é: ", nome)
    idade = int(input("Digite sua idade em anos: "))
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    num3 = int(input("Digite o terceiro numero: "))
    media = (num1 + num2 + num3) /3
    if media >= 8:
        print("Parabens voce esta aprovado!")
    else: 
        print ("seu burro voce nao passou nem tente novamente")
except ValueError:
    print( " informe os dados corretos")
