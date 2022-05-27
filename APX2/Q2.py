def procuraPalvra(arq,palavra):
    conteudo = open(arq, 'r')
    for linha in conteudo:
        dados_da_linha = linha.split()
        for dado in dados_da_linha:
            if dado == palavra:
                print("Linha "+ linha + ", Palavra " + dado + " nesta linha!")
    conteudo.close()

def main():
    arq = input("Insira o nome do arquivo a ser analisado: ")
    palavra = input("Insira a palavra que será buscada: ")

    procuraPalvra(arq,palavra)

main()