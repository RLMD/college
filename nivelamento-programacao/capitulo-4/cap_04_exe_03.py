#Variável na qual será adicionada o número entrado pelo usuário
soma = 0

#Loop realizado 10 vezes. Requisita um número ao usuário para ser somado
for contador in range (1, 11):
    num = float(input("Digite um número: "))
    soma = soma + num

#Exibi o resultado
print(f"A soma dos números é: {soma}")