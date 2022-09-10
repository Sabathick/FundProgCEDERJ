def converte(s):
    numeros = []
    numerosParaSeparar = s.split()
    for n in numerosParaSeparar:
        numeros.append(int(n))
    return numeros

qtdLinhas = int(input("Digite o número de linhas: "))
if qtdLinhas == 0:
    print("Nenhum número foi lido, portanto, sem mínimo e máximo")
else:
    menor = maior = None
    for posLinha in range(qtdLinhas):
        entrada = input("Digite os números da linha: ")
        numeros = converte(entrada)
        for valor in numeros:
            if menor == maior == None:
                menor = maior = valor
            elif valor < menor:
                menor = valor
            elif valor > maior:
                maior = valor
    print("Menor Número: %d e Maior Número: %d" %(menor, maior))