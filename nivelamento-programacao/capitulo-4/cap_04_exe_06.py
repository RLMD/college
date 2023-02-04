#Entrada do número requisitado ao usuário
num = float(input("Insira um número: "))

#Cálculo dos 10 primairos múltiplos
for contador in range (1, 11):
    multiplo = num * contador
    print(f"{num} x {contador} = {multiplo}")