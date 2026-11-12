from mod_inputs import inp_str

def finalizar():
    start = True 
    while start:
        try:
            opcao = inp_str("\nDeseja finalizar o programa? Digite S para [SIM] ou N para [NAO] para executar o programa novamente.")
            if opcao in("s", "S") or opcao in("n", "N"):
                break
            else:
                print("opcao invalida!\n")
        except: 
            print("Opcao Invalida!")
    if opcao in("s", "S"):
        print("\nPrograma Encerrado!")
        return False
    else:
        return True