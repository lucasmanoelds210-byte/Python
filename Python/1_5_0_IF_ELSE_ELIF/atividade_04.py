try:
    temperatura = float(input(" Digite a temperatura: ").replace(",", "."))
    if temperatura < 0:
        print("Congelante")
    elif temperatura >= 0 and temperatura <= 15:
        print("Frio")
    elif temperatura > 15 and temperatura <= 30:
        print("agradavel")
    else:
        print ("Muito quente")
except:
    print("Digite o a temperatura corretamente em numeros!")