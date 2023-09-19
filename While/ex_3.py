'''Faça um programa que solicite números inteiros e determine se eles são ímpares ou pares
enquanto o usuário não digitar -1. Ao final é informado a quantidade de números digitados, exceto
o -1. '''

#Variável
cont = 0

while True:
    num = int(input("Digite um número (-1 para sair): "))

    #Verificação de Par, Ímpar ou Saída
    if (num == -1):
        print(f"A quantidade de números digitados: {cont}")
        print("Saindo...")
        break
        
    elif (num % 2 == 0):
        cont = cont + 1
        print("Par!")

    else:
        cont = cont + 1
        print("Ímpar!")
