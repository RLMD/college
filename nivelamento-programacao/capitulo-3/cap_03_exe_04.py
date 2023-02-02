#Entrada de dados pelo usuário
num_1 = float(input("Insira o primeiro número: "))
operacao = input("Digite a operação que deseja fazer:\n\
+ - adição\n- - subtração\n* - multiplicação\n/ - divisão\n")
num_2 = float(input("Insira o segundo número: "))

#Verifica a operação escolhida, faz o cálculo e mostra o resultado
if operacao == '+':
    resultado = num_1 + num_2
    print("O resultado da operação é {0:.2f}".format(resultado))
elif operacao == '-':
    resultado = num_1 - num_2
    print("O resultado da operação é {0:.2f}".format(resultado))
elif operacao == '*':
    resultado = num_1 * num_2
    print("O resultado da operação é {0:.2f}".format(resultado))
elif operacao == '/':
    resultado = num_1 / num_2
    print("O resultado da operação é {0:.2f}".format(resultado))
else:
    print("Operação inválida.")