def inp_str(mensagem):
    while True:
        try: 
            texto = str (input(mensagem))
            break 
        except:
            print("Valor invalido! Por favor digite um texto.")
    return texto

def inp_int(mensagem):
    while True:
        try: 
            numero = int(input(mensagem))
            break 
        except:
            print("Valor invalido! Por favor digite um numero interiro.")
    return numero

def inp_float(mensagem):
    while True:
        try: 
            numero = float(input(mensagem).replace(",", ","))
            break 
        except:
            print("Valor invalido! Por favor digite um numero.")
    return numero