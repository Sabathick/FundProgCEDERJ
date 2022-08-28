val = []
entrada = 0
result = 0
media = 0
while entrada != "":
    entrada = float(input("Digite um valor: "))
    val.append(entrada)
if entrada == "" and len(val) == 0:
    print("Nenhuma linha lida com conteúdo")
else:
    for i in val:
        result += val(i)
        media = result/len(val)
        print("Soma dos Números: %.2f" % result)
        print("Média dos Números: %.2f" % media)