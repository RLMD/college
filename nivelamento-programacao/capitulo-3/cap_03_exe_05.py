#Entrada dos números da placa pelo usuário
placa = input("Insira o número da placa do seu carro para saber o dia do rodízio. ")

#Verifica o número final da placa e exibe o dia do rodízio correspondente
num_placa = int(placa[-1])

if num_placa == 1 or num_placa == 2:
    print("O dia do seu rodízio é segunda.")
elif num_placa == 3 or num_placa == 4:
    print("O dia do seu rodízio é terça.")
elif num_placa == 5 or num_placa == 6:
    print("O dia do seu rodízio é quarta.")
elif num_placa == 7 or num_placa == 8:
    print("O dia do seu rodízio é quinta.")
elif num_placa == 9 or num_placa == 0:
    print("O dia do seu rodízio é sexta.")