#Entrada do número requisitado ao usuário
num = float(input("Insira um número: "))
final = int(f"{num:.0f}")
fatorial = 1

#Cálculo do Fatorial
for contador in range (1, final + 1):
    fatorial = fatorial * contador

print(f"O fatorial é: {fatorial}")