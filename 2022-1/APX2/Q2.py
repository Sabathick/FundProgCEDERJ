def procuraPalvra(arq,palavra):
    contador = 0
    conteudo = open(arq, 'r')
    for linha in conteudo:
        dados_da_linha = linha.split()
        contador = contador + 1
        for dado in dados_da_linha:
            if dado == palavra:
                print("Linha "+ str(contador) + ", Palavra " + str(dados_da_linha.index(dado)+1) + " nesta linha!")
    conteudo.close()

def main():
    arq = input("Insira o nome do arquivo a ser analisado: ")
    palavra = input("Insira a palavra que será buscada: ")

    procuraPalvra(arq,palavra)

main()