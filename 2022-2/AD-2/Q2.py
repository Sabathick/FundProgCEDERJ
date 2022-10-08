#Sugestão de realizar sem readlines()
#with open("filename.txt", "rb") as f:
#   contents = f.read().decode("UTF-8")
entrada=input("Entre com o nome do arquivo: ")
arq=open("entrada")
linhas=arq.readlines()

print("Conteúdo Ordenado das Palavras e Respectivas Ocorrências: ")
for linha in linhas:
    palavras = linha.split()
    for palavra in palavras:
        if palavra[0] in "AEIOUaeiou":
            with open(arq) as a:
                contador = a.read().count(palavra)
                print(palavra + " ocorre "+contador+"vezes")




