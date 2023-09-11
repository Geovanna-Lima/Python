#Enunciado
'''Escreva um programa que lê dois valores inteiros e exibe os seguintes resultados:
a) o resultado do primeiro número dividido pelo segundo número
b) o resultado da divisão truncada do primeiro número pelo segundo número'''

#Variáveis
n1 = int(input('Digite o número 1:'))
n2 = int(input('Digite o número 2:'))

#Contas
result1 = n1/n2
result2 = n1//n2

#Exibição
print(f'O resultado do primeiro número dividido pelo segundo é: {result1}')
print(f'O resultado da divisão truncada do primeiro número pelo segundo número: {result2}')

