'''Escreva um programa que apresente todos os ímpares de 1 até 99.'''

for i in range(1, 100, 2):
    if i == 99:
        print(i, end = '.')
    else:
        print(i, end = ' , ')
