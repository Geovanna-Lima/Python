'''Faça um programa que calcule e apresente o fatorial de um número inteiro e natural fornecido
pelo usuário.'''

fat = 1
n = int(input("Número inteiro e natural (nao-negativo): "))

while n < 0:
    print("Valor inválido!")
    n = int(input("Número inteiro e natural (nao-negativo): "))
    
for i in range(n, 0, -1):
    fat *= i
    
print(f"Fatorial = {fat}")
    
