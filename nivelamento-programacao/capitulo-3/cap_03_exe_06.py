#Entrada de dado requisitada ao usuário
num = float(input("Insira um número: "))

#Compara o número inserido e exibe o resultado
if num == 0:
    print("O número inserido é nulo.")
elif num > 0:
    print("O número inserido é positivo.")
else:
    print("O número inserido é negativo.")