#Enunciado
'''Escreva um programa que receba três números inteiros quaisquer e apresente:
a) a soma dos quadrados dos três números;
b) o quadrado da soma dos três números.'''

#Biblioteca
import math

#Variáveis
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

#Conta
soma = math.pow(n1,2) + math.pow(n2,2) + math.pow(n3,2)
quadrado = math.pow((n1 + n2 + n3),2)

#Exibição
print(f'A soma dos quadrados dos três números: {soma}')
print(f'O quadrado da soma dos três números: {quadrado}')
