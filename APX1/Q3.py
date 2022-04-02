import re

#a)
def verifica_float(entrada):
    tipo =str(type(entrada))
    if 'float' in tipo:
        return True

#b)
def is_number(entrada):
    try:
        float(entrada)
        return True
    except ValueError:
        return False

def converte_float(entrada):
    if is_number(entrada) == True:
        real_num = float(entrada)
        return real_num
    else:
        invalido_alfabeto = re.search(r'[a-z]', entrada)
        invalido_caracter = re.search(r'..{2}o', entrada)

        if invalido_alfabeto != None:
            return print("Na posição "+ str(invalido_alfabeto)+" há o caracter "+ entrada[invalido_alfabeto])
        if invalido_caracter != None:
             return print("Há mais do que um '.'")
#c)
def conversao(entrada, taxa):
    if verifica_float == True:
        global brl
        brl = round(entrada*taxa, 3)
        print("O valor "+str(entrada)+" com a taxa "+str(taxa)+" vai para "+str(brl))
        return brl

#d)
def desconto():
    global preco_desconto
    preco_desconto = round(brl*0.15, 3)
    print("O valor com desconto é "+str(preco_desconto))

#e)
def parcelamento(vezes):
    if vezes == 1:
        desconto()
        return print("Vocês ganhou 15% de desconto, portanto, de "+str(brl)+" você vai pagar "+str(preco_desconto))
    elif vezes > 1:
        total = round(brl *((1+0.05/100)**vezes) ,2)
        parcelas = round(total/vezes, 2)
        return print("Pagando em "+str(vezes)+" parcelas, e com 5% de juros ao mês, você pagará"+str(parcelas)+" por mês, sendo o total de"+str(total)+" BRL.")


entrada = input("Digite um valor: ")
taxa = input("Digite a taxa de conversão: ")
vezes = input("Digite a quantidade de parcelas: ")

if verifica_float(entrada) and is_number(entrada) == True:
    valor = converte_float(entrada)
    conversao(valor, taxa)
    parcelamento(vezes)
else:
    print("Você digitou errado, "+str(entrada)+" não é do tipo float.")