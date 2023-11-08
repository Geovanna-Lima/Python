'''Escreva um programa em Python que leia duas listas de 20 números inteiros cada e armazene em uma lista de mesmo
tamanho a soma de cada elemento das duas listas. Exibir as três listas.
Faça uma implementação utilizando função. Na implementação com funções NÃO UTILIZE variáveis GLOBAIS'''

# Variáveis
qnt_num = 20

def entrada():
    lista_um = []
    lista_dois = []

    # Pedir lista um
    print(f"Digite {qnt_num} números inteiros da lista 1: ")
    for i in range(qnt_num):
        lUm =  int(input())
        lista_um.append(lUm)

    # Pedir lista dois
    print(f"Digite {qnt_num} números inteiros da lista 1: ")
    for i in range(qnt_num):
        lDois =  int(input())
        lista_dois.append(lDois)

    return(lista_um, lista_dois)


def processamento(lista_um, lista_dois):
    # Soma dos elementos da lista
    lista_tres = []

    for i in range(qnt_num):
        soma = lista_um[i] + lista_dois[i]
        lista_tres.append(soma)
        
    return lista_tres


def saida(lista_um, lista_dois, lista_tres):
    # Exibição
    print(f"Lista 1: {lista_um}")
    print(f"Lista 2: {lista_dois}")
    print(f"Soma: {lista_tres}")

    
lista_um, lista_dois = entrada()
lista_tres = processamento(lista_um, lista_dois)
saida(lista_um, lista_dois, lista_tres)
