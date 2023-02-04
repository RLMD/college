#Entrada do número requisitado ao usuário
num = float(input("Insira um número: "))

#Cálculo dos 10 primeiros múltiplos do número entrado
for contador in range (1, 11):
    mult = num * contador
    print (mult)