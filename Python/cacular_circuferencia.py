import mod_inputs
import mod_sair
import math

def calcular_circuferencia(raio):
    Circuferencia  = 2 * math.pi * raio
    return Circuferencia

start = True
while start:
    raio = mod_inputs.inp_float("O valor do raio e: ")
    break

resultado = calcular_circuferencia(raio)
print("O resultado do calculo: ", resultado)