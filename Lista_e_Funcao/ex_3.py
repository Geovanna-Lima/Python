'''Escreva um programa em Python com a seguinte lista de inteiros:
lista = [13, 41, 13, 8, 21, 7, 79] Calcule
e mostre:
• o valor do maior elemento desta lista (NÃO UTILIZE o max);
• o valor do menor elemento desta lista (NÃO UTILIZE o min);
• o número de vezes que um determinado número, digitado pelo usuário, aparece nesta lista (NÃO UTILIZE o
count)

FAÇA CADA UMA DAS OPERAÇÕES EM UMA FUNÇÃO'''

# Variávies
lista = [13, 41, 13, 8, 21, 7, 79] 

def maior():
    # Maior valor da lista
    maior = lista[0]

    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    return maior


def menor():
    # Menor valor da lista
    menor = lista[0]

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]

    return menor


def contNum(num):
    cont = 0
    
    for i in lista:  
        if i == num:
            cont += 1

    return cont 

print(lista)
num = int(input("Digite o número a ser pesquisado na lista: "))
print(f"Maior elemento: {maior()}")
print(f"Menor elemento: {menor()}")
print(f"Número de ocorrências do número {num} na lista: {contNum(num)}")




