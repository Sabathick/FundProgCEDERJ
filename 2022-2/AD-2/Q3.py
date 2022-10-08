entrada=input("Digte a sequência de números: ")

def mostra_numeros(numeros):
    numerosArr = numeros.split()
    return numerosArr

def menor_numero():
    numerosArr = mostra_numeros(entrada)
    menor = numerosArr[0]
    for numero in numerosArr:
        if numero < menor:
            menor = numero
            return numerosArr.index(numero),numero

def ordena_crescente():
    numerosArr = mostra_numeros(entrada)
    return numerosArr.sort()

def busca_crescente():
    numerosArr = mostra_numeros(entrada)
    numerosArr.sort()
    busca = int(input("Qual elemento você quer buscar? "))
    repetidos = []
    for numero in numerosArr:
        if numero == busca:
            repetidos.append(numerosArr.index(numero))
    return repetidos, busca
print("A entrada é: "+ mostra_numeros(entrada))
pos, menor = menor_numero(entrada)
print("O menor elemento da sequência da entrada é "+pos+", ele está na posição "+menor)
print("Ordenando a sequência, temos: "+ordena_crescente(entrada))
pos, busca = busca_crescente(entrada)
print("Elemento "+busca+" está na posição "+pos[0])
print("Além da posição "+pos[0]+" todas as posições que contém o elemento "+busca+" são: ")
pos.pop()
print(*pos)
