#Entrada dos valores do produto e da porcentagem pelo usuário
valor = float(input("Digite o valor do produto: "))
num_porcentagem = float(input("Digite a porcentagem: "))

#Cálculo da porcentagem
porcentagem = num_porcentagem * 0.01
valor_pocentagem = valor * porcentagem

#Cálculo do acréscimo
acrescimo = valor * (porcentagem + 1)

#Cálculo do desconto
desconto = valor * (1 - porcentagem)

#Exibição dos resultados
print("O valor da porcentagem é: R${0:.2f}\n\
O valor final com acréscimo é: R${1:.2f}\n\
O valor final com desconto é: R${2:.2f}".format(valor_pocentagem, acrescimo, desconto))