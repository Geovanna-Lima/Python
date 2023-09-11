'''Faça um programa que coloque dois nomes em ordem alfabética.'''

#Variáveis
nome1 = input("Digite o primeiro nome:").lower() #Deixa variável minúscula
nome2 = input("Digite o segundo nome:").lower()

if (nome1 == nome2):
    print("Nomes iguais!")

else:
    if (nome1 > nome2):
        print(f'Os nomes em ordem alfabética são: {nome2}, {nome1}')

    else:
        print(f'Os nomes em ordem alfabética são: {nome1}, {nome2}')
