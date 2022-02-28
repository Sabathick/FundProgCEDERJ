#Programa para retornar o troco dos valores comas maiores cédulas possiveis

val = []
entrada = 0
#Obtendo as entradas e validando se os valores são inteiros
while entrada >= 0:
    entrada = int(input("Digite um valor: "))
    if entrada > 0:
        val.append(entrada)
    else:
        print("Valor inválido!")
        break

print(val)

for i in val:
    print("Trocando "+val[i]+" em:\n")

    #Teste para notas de 100
    result = val[i]/100
    resto = val[i] % 100
    if result == 1:
        print(result+" nota de 100 reais")
    if result > 1:
        print(result+" notas de 100 reais")
    #Teste para notas de 50
    result = resto/50
    resto = result % 50
    if result == 1:
        print(result+" nota de 50 reais")
    if result > 1:
        print(result+" notas de 50 reais")
    #Teste para notas de 20
    result = resto/20
    resto = result % 20
    if result == 1:
        print(result+" nota de 20 reais")
    if result > 1:
        print(result+" notas de 20 reais")
    #Teste para notas de 10
    result = resto/10
    resto = result % 10
    if result == 1:
        print(result+" nota de 10 reais")
    if result > 1:
        print(result+" notas de 10 reais")
    #Teste para notas de 5
    result = resto/5
    resto = result % 5
    if result == 1:
        print(result+" nota de 5 reais")
    if result > 1:
        print(result+" notas de 5 reais")
    #Teste para notas de 2
    result = resto/2
    resto = result % 2
    if result ==1:
        print(result+" nota de 2 reais")
    if result > 1:
        print(result+" notas de 2 reais")
    if resto == 1:
        print(resto+" moeda de 1 real")
    if result > 1:
        print(resto+" moedas de 1 real")