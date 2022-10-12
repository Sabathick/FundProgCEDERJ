entrada=input("Entre com o nome do arquivo: ")

def abrir(arquivo):
    arquivo=open("entrada",encoding="utf-8")
    linhas = []
    for linha in arquivo:
        linhas.append(linha)
    arquivo.close()
    return linhas

print("Conteúdo Ordenado das Palavras e Respectivas Ocorrências: ")
conteudo = abrir(entrada)
for linha in conteudo:
    palavras = linha.split()
    for palavra in palavras:
        if palavra[0] in "AEIOUaeiou":
            with open(entrada) as a:
                contador = a.read().count(palavra)
                print(palavra + " ocorre "+contador+"vezes")




