'''Escreva um programa que apresente os n(1 <= n <= 20) primeiros termos da seguinte sequência:
1, 4, 9, 16, 25, ...'''

x = 1
n = int(input("Digite a quantidade de elementos: "))

while n < 1 or n > 20:
    n = int(input("Digite a quantidade de elementos: "))
    
for cont in range(n):
    print(x**2)
    x += 1
    

    
