entrada = (input("Digite um valor: "))
if entrada == "":
    print("Nenhuma linha lida com conteúdo")
else:
    soma = 0
    qtd = 0
    while entrada != "":
        soma += float(entrada)
        qtd += 1
        entrada = (input("Digite um valor: "))
        print("Soma dos Números: %.2f" %soma)
        print("Média dos Números: %.2f" %(soma/qtd))