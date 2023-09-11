#Enunciado
'''Faça um programa que receba o custo de um espetáculo teatral e o preço do ingresso desse
espetáculo. Esse programa deve calcular e mostrar:
a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo
seja alcançado.
b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.'''

#Biblioteca
import math

#Variáveis
custo = float(input('Digite o custo do espetáculo teatral:'))
ingresso = float(input('Digite o preço do ingresso:'))

#Conta
convites_vendidos = math.ceil(custo/ingresso)
lucro = custo + (custo * 0.23)
convites_lucro = math.ceil(lucro/ingresso)

#Exibição
print(f'Mínimo de ingressos: {convites_vendidos}')
print(f'O valor com o lucro de 23% é: R${lucro}')
print(f'Ingresso para ter lucro de 23%: {convites_lucro}')
