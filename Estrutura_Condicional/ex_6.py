'''Dado o preço de um produto (inteiro), elabore um programa que calcule e
apresente a menor quantidade de notas (de cada valor) necessárias para efetuar o
pagamento da compra desse produto.
Só apresente as notas que serão utilizadas, ou seja, se para pagar o valor você não
utilizar a nota de 5, ela não deverá ser apresentada.
Considere como valores de notas: 1, 2, 5, 10, 20, 50, 100.'''

#Variáveis
num = int(input("Digite o preço do seu produto:"))

#Notas de 100
nota100 = num // 100
resto1 = num % 100

#Notas de 50
nota50 = resto1 // 50
resto2 = resto1 % 50

#Notas de 20
nota20 = resto2 // 20
resto3 = resto2 % 20

#Notas de 10
nota10 = resto3 // 10
resto4 = resto3 % 10

#Notas de 5
nota5 = resto4 // 5
resto5 = resto4 % 5

#Notas de 2
nota2 = resto5 // 2
resto6 = resto5 % 2

#Notas de 1
nota1 = resto6 // 1

#Exibição das notas
if (nota100 != 0):
    print(f"Nota de 100: {nota100}")

if (nota50 != 0):
    print(f"Nota de 50: {nota50}")

if (nota20 != 0):
    print(f"Nota de 20: {nota20}")

if (nota10 != 0):
    print(f"Nota de 10: {nota10}")

if (nota5 != 0):
    print(f"Nota de 5: {nota5}")

if (nota2 != 0):
    print(f"Nota de 2: {nota2}")

if (nota1 != 0):
    print(f"Nota de 1: {nota1}")
