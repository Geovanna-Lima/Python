'''Faça um programa que solicite 5 números inteiros e determine se eles são ímpares ou pares.'''

#Variáveis
cont = 0

while (cont < 5):
    cont = cont + 1
    num = int(input("Digite um número: "))

    #Verificação de Par ou Ímpar
    if (num % 2 == 0):
        print("Par!")

    else:
        print("Ímpar!")
