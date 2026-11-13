import mod_inputs
import mod_sair
import math

def calculo_imc(peso, altura):
     imc = peso / math.pow(altura, 2)
     return imc

def valida_idade():
    while True:
        try:
            idade = mod_inputs.inp_int("Digite sua idade: ")
            if idade <20:
                print("sua idade deve ter no minimo 20 anos")
            else:
                break
        except:
            print("digite apenas numeros!")
    return idade

def classificacao(imc, idade):
    while True:
        if idade >= 20 and idade <= 60:
            
            if imc < 18.5:
                mensagem = "Abaixo do peso"
            elif imc >18.5 and imc <=24.9:
                mensagem = "normal"
            elif imc >= 25.0 and imc <=29.9:
                mensagem = "Sobrepeso"
            else:
                print("Obesidade Morbida")
        break
start = True
while start:
    nome = mod_inputs.inp_str("Digite seu nome: ")
    idade = valida_idade()
    peso = mod_inputs.inp_float("Digite seu peso: ")
    altura = mod_inputs.inp_float("Digite sua altura: ")
    imc = calculo_imc(peso, altura)
    nivel = classificacao(imc,idade)
    print("O nome do cliente e: ", nome)
    print("A idade do cliente e: ", idade)
    print("O peso do cliente e: ", peso)
    print("A altura do cliente e: ", altura)
    start = mod_sair.finalizar()