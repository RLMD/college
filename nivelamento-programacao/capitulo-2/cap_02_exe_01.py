#Entrada dos números feitas pelo usuário
num_1 = float(input("Insira o primeiro número: "))
num_2 = float(input("Insira o segundo número: "))
num_3 = float(input("Insira o terceiro número: "))
num_4 = float(input("Insira o quarto número: "))

#Cálculo da média dos números
media = (num_1 + num_2 + num_3 + num_4) / 4

#Exibição do resultado
print("A média dos números é {0:.2f}".format(media))