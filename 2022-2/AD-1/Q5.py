def compara_string():
    primeira = input("Digite a primeira string: ")
    segunda = input("Digite a segunda string: ")
    primeira_array = primeira.split()
    segunda_array = segunda.split()
    if len(primeira_array) < len(segunda_array):
        for i in primeira_array:
            set(segunda_array)