import mod_inputs 
import mod_sair
start = True 
while start: 
    nome = mod_inputs.inp_str("\nDigite o seu nome: ")
    idade = mod_inputs.inp_int("\nDigite sua idade emm anos: ")
    peso = mod_inputs.inp_float("\nDigite seu peso em kg: ")

    print("\n========== Dados Informados ==========")
    print("Seu nome e ", nome)
    print("Voce possui", idade, "anos.")
    print("Seu peso e", peso, "kg.")

    start = mod_sair.finalizar()