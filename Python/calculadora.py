import math
import mod_inputs
import mod_sair

def valida_opcao():
    while True:
        print("Digite / para divisao")
        print("Digite * para multiplicacao")
        print("Digite + para adicao")
        print("Digite - para subtracao")
        
        opcao = mod_inputs.inp_str("Digite uma opcao: ")
        if opcao in ("/", "*", "+", "-"):
            break
        else:
            print("Opcao invalida!")
    return opcao

def calculadora(num1, num2, opcao):
    match opcao: 
        case "/":
            resultado = num1 / num2
        case "*": 
            resultado = num1 * num2 
        case "+":
            resultado = num1 + num2 
        case "-":
            resultado = num1 - num2 
    return resultado 
start = True
while start: 
    num1 = mod_inputs.inp_float("Digite o primeiro numero: ")
    num2 = mod_inputs.inp_float("Digite o segundo numero: ")
    opcao = valida_opcao()
    calculo = calculadora(num1, num2, opcao)
    print("O resultado de ", num1, opcao, num2, "é = ", calculo)
    start = mod_sair.finalizar()