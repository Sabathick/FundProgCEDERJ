def maior_que(linhas):
    ordem = []
    for i in linhas:
        numeros = input("Digite os valores desta linha:")
        if numeros != "":
            ordem.append(map(int, numeros.split()))
            print("Menor Número: "+min(ordem)+" e Maior Número: "+max(ordem))
        else:
            print("Nenhum número foi lido, portanto, sem mínimo e máximo!!")

maior_que()