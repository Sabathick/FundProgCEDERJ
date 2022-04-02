#A primeira linha é a quantidade de testes qtdTestes
#A segunda linha é a quantidade de valores de cada teste qtdValoresTeste
#Na terceira um valor mínimo de um intervalo de valores
#Na quarta, o valor máximo do intervalo

valores = []
abaixo = 0
acima = 0
dentro = 0
soma = 0
val = None
qtdTestes = int(input("Digite a quantidade de testes: "))
qtdValoresTeste = int(input("Digite a quantidade de valores em cada teste: "))
min = float(input("Digite o valor mínimo do intervalo: "))
max = float(input("Digite o valor máximo do intervalo: "))

for i in range(qtdValoresTeste):
    val = float(input("Insira o "+str(i)+"º do teste: "))
    valores.append(val)
    if valores[i] < min:
        abaixo = abaixo + 1
    elif valores[i] > min and valores[i] < max:
        dentro = dentro + 1
        soma = soma + valores[i]
    elif valores[i] > max:
        acima = acima + 1
    else:
        break 

for i in range(qtdTestes):
    print("Teste "+str(i)+":")
    print("     Abaixo do Intervalo: "+str(abaixo)+", No intervalo: "+str(dentro)+",\n Acima do Intervalo: "+str(acima)+".")
    print("     Soma dos Valores Dentro do Intervalo: "+str(soma))
