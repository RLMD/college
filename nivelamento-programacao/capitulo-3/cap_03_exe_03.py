#Entrada de dado pelo usuário
num = int(input("Digite um número entre 1 e 7 para saber qual é o dia da semana. "))

if num == 1:
    print("Hoje é domingo.")
elif num == 2:
    print("Hoje é segunda.")
elif num == 3:
    print("Hoje é terça.")
elif num == 4:
    print("Hoje é quarta.")
elif num == 5:
    print("Hoje é quinta.")
elif num == 6:
    print("Hoje é sexta.")
elif num == 7:
    print("Hoje é sábado.")
else:
    print("Número inválido.")