#Entrada de dado pelo  usuário
num = float(input("Insira um número: "))

#Verifica se o número é negativo ou não e apresenta o resultado
if num < 0:
    modulo = num * (-1)
    print(f"O módulo desse número é: {modulo}")
else:
    print(f"O módulo desse número é: {num}")