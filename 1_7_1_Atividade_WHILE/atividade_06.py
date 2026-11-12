soma = 0
contador = 0

nota = float(input("Digite uma nota (-1 para encerrar): "))

while nota != -1:
    soma = soma + nota
    contador = contador + 1

    nota = float(input("Digite uma nota (-1 para encerrar): "))

if contador > 0:
    media = soma / contador
    print("A média das notas é:", media)
else:
    print("Nenhuma nota foi informada.")