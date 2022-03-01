#Programa para retornar o troco dos valores comas maiores cédulas possiveis

val = []
entrada = 0
i = 0
#Obtendo as entradas e validando se os valores são inteiros
while i >= 0:
    entrada = input("Digite um valor: ")
    if entrada != '':
        entrada = int(entrada)
    else:
        break
    if entrada > 0:
        val.append(entrada)
        i += 1
    else:
        print("Valor inválido!")
        break

print(val)

for i in range(0,len(val)):
    print("Trocando "+str(val[i])+" em:")

    #Teste para notas de 100
    resto = int(val[i] % 100)

    if val[i] >= 100:
        result = int(val[i]/100)
        if result == 1:
            print("     "+str(result)+" nota de 100 reais")
        if result > 1:
            print("     "+str(result)+" notas de 100 reais")

    #Teste para notas de 50
    if resto >= 50:
        result = int(resto/50)
        resto = int(resto % 50)
        if result == 1:
            print("     "+str(result)+" nota de 50 reais")
        if result > 1:
            print("     "+str(result)+" notas de 50 reais")

    #Teste para notas de 20
    if resto >= 20:
        result = int(resto/20)
        resto = int(resto % 20)
        if result == 1:
            print("     "+str(result)+" nota de 20 reais")
        if result > 1:
            print("     "+str(result)+" notas de 20 reais")
    
    #Teste para notas de 10
    if resto >= 10:
        result = int(resto/10)
        resto = int(resto % 10)
        if result == 1:
            print("     "+str(result)+" nota de 10 reais")
        if result > 1:
            print("     "+str(result)+" notas de 10 reais")

    #Teste para notas de 5
    if resto >= 5:
        result = int(resto/5)
        resto = int(resto % 5)
        if result == 1:
            print("     "+str(result)+" nota de 5 reais")
        if result > 1:
            print("     "+str(result)+" notas de 5 reais")
    
    #Teste para notas de 2
    if resto >= 2:
        result = int(resto/2)
        resto = int(resto % 2)
        if result ==1:
            print("     "+str(result)+" nota de 2 reais")
        if result > 1:
            print("     "+str(result)+" notas de 2 reais")
    if resto >= 1:
        if resto == 1:
            print("     "+str(result)+" moeda de 1 real")
        if result > 1:
            print("     "+str(result)+" moedas de 1 real")