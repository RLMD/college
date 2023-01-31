#Dados entrados pelo usuário
preco_maco = float(input("Insira o preço do maço de cigarros: R$"))
qtd_por_dia = int(input("Insira quantos maços você consome por dia: "))
num_anos = int(input("Insira há quantos anos você fuma: "))

#Cálculo de quanto foi gasto em cigarros
num_dias = num_anos * 365
total_gasto = num_dias * preco_maco

#Exibição do resultado
print("Você gastou R${0:.2f} fumando.".format(total_gasto))