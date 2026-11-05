try:
    precoProd = float(input ("digite o preço do produto: "))
    descontoporcentual = float(input ("digite o desconto: "))
    descontototal = precoProd * (descontoporcentual / 100)
    precofinal2 = precoProd - descontototal

    print("preco final", precofinal2)
except ValueError:
    print("digite os valores corretos novamente")
