
def ler_num():
    linhas = []
    entrada = 0
    contador = 0
    media = 0
    while entrada != "":
        entrada = input("Digite uma linha: ")
        linhas.append(entrada)
    linhas.pop()
    for linha in linhas:
        partes = linha.split(' ')
        for parte in partes:
            contador += 1 
            media = media + float(parte)
            partes.sort()
        print("Menor: "+partes[0]+" Maior: "+partes[len(partes)-1])
    print("Quantidade de Números Lidos: "+str(contador))
    print("Média dos Números Lídos: "+str(media/contador))
    
    if linhas == "":
        print("Nenhum Número Foi Lido. Portanto, não existe média!!!")


ler_num()
