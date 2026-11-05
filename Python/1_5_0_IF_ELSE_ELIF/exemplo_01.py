try: 
    idade = int(input("digite sua idade em anos: "))
    if idade < 18 and idade >= 16: 
        print("Para entrar no sistema e necessario ser maior que 18 anos ")
except:
    print(" idade invalida complete 18 anos e tente novamente ")
