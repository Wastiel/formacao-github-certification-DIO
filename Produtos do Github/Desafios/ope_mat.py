# 3 - Descrição: solicitar dois numeros e realizar uma operação matematica simples

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite um número inteiro: '))

operacao = input("Digite a operação que deseja realizar: (+, -, *, /): ")

if operacao == '+':
    print("soma: " + str(numero1 + numero2))
elif operacao == '-':
    print("subtração: " +  str(abs(numero1 - numero2)))
elif operacao == '*':
    print("multiplicação: " + str(numero1 * numero2))
elif operacao == '/':
    print("divisão: " + str(numero1 / numero2))
else:
    print("Operação inválida")


