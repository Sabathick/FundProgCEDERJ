def separa_nome():
    lista_nomes = []
    nomes_separados = []
    sobrenomes_separados= []
    qtd = int(input("Digite a quantidade de nomes: "))
    for nome in range(qtd):
        nome = input("Digite o nome completo: ")
        lista_nomes = nome.split(' ')
        nomes_separados.append(lista_nomes[0])
        sobrenomes_separados.append(lista_nomes[len(lista_nomes)-1])
        lista_nomes = []
    for i in nomes_separados:
        print(nomes_separados[i]+" "+sobrenomes_separados[i])
    

separa_nome()