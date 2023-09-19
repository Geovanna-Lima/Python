'''Faça um programa que solicite números inteiros e determine a soma e quantidade de números
digitados enquanto o usuário não digitar -1. Ao final é informado a soma e quantidade de números
digitados, exceto o -1.'''

#Variável
cont = 0
soma = 0

while True:
    num = int(input("Digite um número (-1 para sair): "))

    #Verificação de Par, Ímpar ou Saída
    if (num == -1):
        print(f"A quantidade de números digitados: {cont}")
        print(f"A soma dos números digitados: {soma}")
        print("Saindo...")
        break

    else:
        cont += 1
        soma += num
