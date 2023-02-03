#Candidatos
huguinho = 0
zezinho = 0
luizinho = 0
#Variável para finalização da votação
finaliza = 1

#Votação fica em loop até que seja digitado 0
while finaliza != 0:
    voto = int(input("Digite o número do seu candidato.\n1 - Huguinho\n2 - Zezinho\n3 - Luizinho\n0 - Encerrar votação.\n"))

    #Verifica o voto dado pelo usuário e adiciona 1 a contagem de votos do candidato correspondente
    if voto == 1:
        huguinho =+ 1
    elif voto == 2:
        zezinho =+ 1
    elif voto == 3:
        luizinho =+ 1
    elif voto == 0:
        finaliza = 0
    else:
        voto = int(input("Número inválido.\nDigite o número do seu candidato.\n1 - Huguinho\n2 - Zezinho\n3 - Luizinho\n0 - Encerrar votação.\n"))
        if voto == 0:
            finaliza = 0

#Exibe o resultado
print(f"O resultado da votação é:\nHuguinho - {huguinho} votos.\nZezinho - {zezinho} votos.\nLuizinho - {luizinho} votos.")
