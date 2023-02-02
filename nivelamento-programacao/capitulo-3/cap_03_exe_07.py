#Entrada de dados requisitadas ao usuário
num_1 = float(input("Insira o primeiro número: "))
num_2 = float(input("Insira o segundo número: "))
num_3 = float(input("Insira o terceiro número: "))

maior_num = num_1

#Compara os números e exibe o maior deles
if num_2 > maior_num:
    maior_num = num_2
    if num_3 > maior_num:
        maior_num = num_3

print(f"O maior número é {maior_num}.")
