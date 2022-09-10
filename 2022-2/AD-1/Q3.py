def contarVogais(linha):
    total = 0
    for char in linha:
        if char in "AEIOUaeiou":
            total += 1
    return total

def pegaMaisComprida(linha):
    maior= ""
    palavrasNaLinha = linha.split()
    for palavra in palavrasNaLinha:
        if len(palavra) > len(maior):
            maior = palavra
    return maior

def palindromo(palavra):
    for i in range(len(palavra) // 2):
        if palavra[i] != palavra[len(palavra) -1 -i]:
            return False
    return True

def contarPalindromos(linha):
    total = 0
    palavrasNaLinha = linha.split()
    for palavra in palavrasNaLinha:
        if palindromo(palavra):
            total += 1
    return total

entrada = input("Digite sua frase:")
if entrada == "":
    print("Nenhuma linha não vazia foi lida!!")
else:
    palavraMaisComprida = ""
    maisVogais = entrada
    qtdMaisVogais = contarVogais(entrada)
    comMaisPalindromos = ""
    qtdMaisPalindromas = -1
    while entrada != "":
        qtdAtual = contarVogais(entrada)
        if qtdAtual > qtdMaisVogais:
            maisVogais = entrada
            qtdMaisVogais = qtdAtual
        palMaisCompridaAtual = pegaMaisComprida(entrada)
        if len(palMaisCompridaAtual) > len(palMaisComprida):
            palMaisComprida = palMaisCompridaAtual
        qtdMaisPalindromosAtual = contarPalindromos(entrada)
        if qtdMaisPalindromosAtual > qtdMaisPalindromos:
            comMaisPalindromos = entrada
            qtdMaisPalindromos = qtdMaisPalindromosAtual
        entrada = input()
    print("Linha com mais vogais sem acento:", maisVogais)
    print("Quantidade de vogais sem acento:", qtdMaisVogais)
    print()
    print("Palavra de maior comprimento lida:", palMaisComprida)
    print()
    print("Linha com mais Palíndromes:", comMaisPalindromos)
    print("Quantidade de palavras Palíndromes:", qtdMaisPalindromos)