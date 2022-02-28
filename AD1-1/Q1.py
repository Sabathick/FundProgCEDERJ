#Programa para retornar o troco dos valores comas maiores cédulas possiveis

val = []
#Obtendo as entradas e validando se os valores são inteiros
while i != "":
    val[i] = int(input("Digite um valor: "))
    if val[i] <= 0:
        print("Valor menor que zero!")
        exit()
    else:
        i = i +1


