try:
    nota = float(input("Digite sua nota em numeros: "))
    if nota < 0 :
        print("nota invalida")
    elif nota > 10 :
        print("nota invalida")
    elif nota >= 0 and nota <= 4.9:
        print("Reprovado")
    elif nota >= 5 and nota <= 6.9:
        print("recuperacao")
    elif nota >= 7 and nota <= 10:
        print("aprovado")
except:
    print("digite apenas numeros ")
