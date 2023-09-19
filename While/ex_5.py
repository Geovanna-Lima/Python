'''Programa que lê um inteiro positivo n e imprime o valor da soma destes números: 1 + 2 + 3 + ... +
n.'''

#Variáveis
soma = 0
cont = 0

#Inserir número
num = int(input("Digite um número: "))


if (num < 0):
    print("Número inválido!")

else:
    while (cont <= num):
        soma += cont
        cont += 1

    print(f"A soma desses números é: {soma}")
