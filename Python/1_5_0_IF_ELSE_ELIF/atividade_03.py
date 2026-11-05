try:
    valor = float(input(" Valor da compra: ").replace(",", "."))
    if valor <= 0:
        print("Compra inválida!")
    elif valor <= 100:
        print("Sem desconto!")
        print("Valor da compra: ", valor)
    elif valor > 100 and valor <= 500: 
        vl_desc = valor * (1-(10/100))
        print ("Voce teve um desconto de 10%!")
        print("Valor da compra: ", vl_desc)
    else:
        vl_desc2 = valor * (1-(15/100))
        print("Desconto de 15%")
        print("Valor da compra: ", vl_desc2)
except:
    print("Digite o valor corretamente em numeros!")