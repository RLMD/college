#Entrada de notas feitas pelo usuário
n_1 = float(input("Digite a primeira nota: "))
n_2 = float(input("Digite a segunda nota: "))
n_3 = float(input("Digite a terceira nota: "))

#Cálculo da média das notas
media = (n_1 + n_2 + n_3) / 3

#Mostra o resultado
print("A média do aluno é {0:.2f}".format(media))