'''Faça um programa que solicite números inteiros e determine se eles são ímpares ou pares
enquanto o usuário não digitar -1.'''

while True:
    num = int(input("Digite um número (-1 para sair): "))

    #Verificação de Par, Ímpar ou Saída
    if (num == -1):
        print("Saindo...")
        break
        
    elif (num % 2 == 0):
        print("Par!")

    else:
        print("Ímpar!")
