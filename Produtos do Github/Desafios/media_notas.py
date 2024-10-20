#5 - Calculando Média de Notas 📚
#Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

#O que aprenderemos?
#Uso de variáveis para armazenar dados fornecidos pelo usuário.
#Aplicação de operadores aritméticos (+, /) para calcular a média de um conjunto de valores.
#Prática na solicitação e manipulação de entrada do usuário.

nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))
nota3 = int(input('Digite a nota 3: '))

total = nota1 + nota2 + nota3

print("a média das notas é: " + str(abs(total/3)) + "." )

