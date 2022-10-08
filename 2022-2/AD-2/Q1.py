entrada=input("Entre com o nome do arquivo: ")
arquivo=open("entrada")
linhas = arquivo.readlines()

def mostrar_conteudo(linhas):
    print("Conteúdo do arquivo: "+entrada)
    for linha in linhas:
        print(linha)

def media_conteudo(linhas):
    media = 0
    for linha in linhas:
        media += media + linha
    media = media/linhas(len)
    print("Média dos números contidos no arquivo: "+media)
    return media

def remove_conteudo(linhas):
    for linha in linhas:
        if linha < media_conteudo(linhas):
            del(linhas[linha])
    print("Conteúdo do arquivo: "+entrada)
    for linha in linhas:
        print(linha)
    
mostrar_conteudo(linhas)
media_conteudo(linhas)
remove_conteudo(linhas)
