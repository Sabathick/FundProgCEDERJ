import os
from pathlib import Path

def mostrar(nm):
    dados = open(nm, "r")
    for linha in dados:
        print("\t", linha.strip())
    dados.close()
    print()
    return None

def verifica_primo(nums):
    divisores = 0
    result = []
    for num in nums:
        num = int(num)
        if num > 0:
            for i in range(num):
                if num%(i+1) == 0:
                    divisores +=1
        else:
            result.append(False)
        if divisores == 2:
            result.append(True)
        else:
            result.append(False)
        
        divisores = 0
    return result

def procura_primo(doc):
    print("Conteúdo do Arquivo "+doc+":")
    mostrar(doc)
    conteudo = open(doc,'r+')
    temp = open("temp.txt", 'w+')
    caminho = Path("temp.txt").absolute()
    for linha in conteudo:
        dados = linha.split()
        if any(verifica_primo(dados)):
            pass
        else:
            temp.write(str(dados)+'\n')

    
    print("Conteúdo do Arquivo "+doc+" após eventuais remoções:")
    os.replace(caminho,doc)
    for linha in conteudo:
        linha = linha.replace('[','')
        linha = linha.replace(',',' ')
        print(linha)
        
    conteudo.close()
    temp.close()
                   
    return None

def main():
    arq = input("Insira o nome do arquivo: ")
    procura_primo(arq)

main()