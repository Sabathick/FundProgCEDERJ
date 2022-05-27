import os

def verificaPrimo(num):
    divisores = 0
    if num > 0:
        for i in range(num):
            if num%(i+1) == 0:
                divisores +=1
    else:
        return False
    if divisores == 2:
        return True
    else:
        return False

def procuraPrimo(doc):
    print("Conteúdo do Arquivo "+doc+":")
    conteudo = open(doc, 'r+')
    temp = open("temp.txt", 'w+')
    for linha in conteudo:
        dados = linha.split()
        for dado in dados:
            if verificaPrimo(dado) == False in linha:
                temp.write(linha)
    
    os.replace(temp, doc)            
    print("Conteúdo do Arquivo "+doc+" após eventuais remoções:")
    conteudo.close()

def main():
    arq = input("Insira o nome do arquivo: ")
    procuraPrimo(arq)

main()