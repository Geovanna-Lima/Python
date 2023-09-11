'''Faça um programa que apresente se o número que o usuário digitou é divisível
por 3 e por 5 ao mesmo tempo.'''

#Variáveis
num = int(input("Digite um número:"))

if (num % 3 == 0 and num % 5 == 0):
    print("Número divisível por 3 e 5!")

else:
    print("Número não divisível por 3 e 5!")
