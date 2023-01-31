numero = int(input("Digite um número: "))
primo_contador = 0

#Divisão por todos os números até o número inserido pelo usuário para verificação
for contador in range (1, numero + 1):
    if numero % contador == 0:
        primo_contador =  primo_contador + 1

#Exibição do resultado
if primo_contador == 2:
    print("Este número é primo.")
else:
    print("Esse número não é primo.")