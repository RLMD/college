#Entrada do número feita pelo usuário
num = float(input("Digite um número.\nCaso deseje encerrar a operação, digite 0: "))

soma = 0

#Verifica se o número entrado é diferente de 0.
#Caso seja, o valor é adicionado.
while num != 0:
    soma = soma + num
    num = float(input("Digite um número.\nCaso deseje encerrar a operação, digite 0: "))

print(f"A soma dos números é: {soma}")