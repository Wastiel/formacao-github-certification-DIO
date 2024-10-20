#6 - Verificando Palíndromos 🔄
#Descrição: Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

#O que aprenderemos?

#Manipulação de strings em Python, especialmente invertendo uma string.
#Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo.
#Introdução ao conceito de palíndromos e sua aplicação em problemas de programação.

palavra = input('Digite uma palavra: ')
palindromo = palavra[::-1]

if palavra.isalpha():
    if (palavra == palindromo):
        print("A palavra " +palavra+ " é palindromo! ")
    else:
        print("A palavra " +palavra+ " não é palindromo! ")
else:
    print("Erro: a string contém números ou caracteres especiais.")
