''' Faça um programa que leia um vetor de 5 números inteiros e mostre-os. O usuário deve
entrar com os valores pelo teclado e o programa deverá imprimir a lista.
Dica: utilize a função append() em python para inserir elementos no vetor. '''

#Variáveis
vetor = []

for i in range(5):
    num = int(input("Digite o número: "))
    vetor.append(num)

print("O resultado do vetor é:")
for i in range(len(vetor)):
    print(f"{vetor[i]}")

