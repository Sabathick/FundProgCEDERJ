def verifica_inteiro(b, exp):
    if type(b) and type(exp) != int:
        print("Base "+b+" e expoente "+exp+" não estão no formato devido")
        return False
    elif type(exp) != int:
        print("Expoente "+exp+ " não está no formato devido")
        return False
    elif type(b) != int:
        print("Base " + b +" não está no formato devido")
        return False
    else:
        return True
def exponencial(b, exp):
    if verifica_inteiro(b,exp) == True:
         if exp == 0:
            return 1
    
    return b * b(exp - 1)

def main():
    b = input("Insira o valor da Base: ")
    exp = input("Insira o valor do expoente: ")
    if exponencial(b,exp) != "":
        print(b+" elevado a "+exp+" é igual a" +exponencial(a,exp))

main()