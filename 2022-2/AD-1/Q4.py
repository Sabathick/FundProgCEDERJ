def expoencial(b, exp):
    if exp == 0:
        return 1
    else:
        return b*expoencial(b,exp-1)

def verifica_inteiro(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False

base = input("Insira o valor: ")
potencia = input("Insira o expoente: ")

if verifica_inteiro(base) and verifica_inteiro(potencia):
    result = expoencial(int(base), int(potencia))
    print(f"{base} elevado a {potencia} é igual a {result}")
elif verifica_inteiro(base) is False and verifica_inteiro(potencia) is False:
    print(f"Base {base} e expoente {potencia} não estão no formato devido")
elif verifica_inteiro(base) is False:
    print(f"Base {base} não está no formato devido")
else:
    print(f"Expoente {potencia} não está no formato devido")
