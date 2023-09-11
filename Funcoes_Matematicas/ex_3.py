#Enunciado
'''Calcule e apresente o volume de uma lata de óleo (v = pi*r^2*altura)'''

#Biblioteca
import math

#Variáveis
raio = float(input('Digite o raio da lata:'))
altura = float(input('Digite a altura da lata:'))

#Conta
volume = math.pi * math.pow(raio,2) * altura

#Exibição
print(f'O volume da lata é: {volume}')
