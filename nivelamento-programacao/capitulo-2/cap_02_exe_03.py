#Quantia em dinheiro informada pelo usuário
quantia = int(input("Insira a quantia em dinheiro a ser trocada: R$"))

#Cálculo de quantas cédulas de 10, 20 e 50 formam a quantia informada
nota_50 = quantia // 50
quantia = quantia % 50
nota_20 = quantia // 20
quantia = quantia % 20
nota_10 = quantia // 10

#Exibição do resultado
print(f"Você receberá {nota_50} notas de R$50,00, {nota_20} notas de R$20,00 e {nota_10} notas de R$10,00.")