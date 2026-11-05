try:
    idade = int(input("Digite sua idade em anos: "))
    if idade <= 0:
        print("Idade Invalida")
    elif idade > 0 and idade <= 12: 
        print("Voce e uma crianca")
    elif idade >= 13 and idade <= 17: 
        print("Voce e um adolescente")
    else:
        print("voce e uma adulto")
except: 
    print("digite apenas numeros")
