'''Faça um programa que apresenta o maior de dois números inteiros (diferentes)
lidos do usuário'''

#Variáveis
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))

if (n1 == n2):
    print("Números iguais!")

else:
    if (n1 > n2):
        print("O primeiro número é maior que o segundo!")

    else:
        print("O segundo número é maior que o primeiro!")

