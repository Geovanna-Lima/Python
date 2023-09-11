'''Faça um programa que leia um número inteiro (e diferente de zero) e mostre
uma mensagem indicando se este número é positivo ou negativo'''

#Variáveis
num = int(input("Digite um número:"))

if (num == 0):
    print("Número não permitido!")
    
else:
    if (num > 0):
        print("Número positivo!")

    else:
        print("Número negativo!")
