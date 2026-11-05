try: 
    idade = int(input("digite sua idade em anos: "))
    if idade < 18 :
        print("Para entrar no sistema e necessario ser maior que 18 anos ")
    else:
        print("voce faz parte da terceira idade")
except:
    print(" idade invalida complete 18 anos e tente novamente ")
