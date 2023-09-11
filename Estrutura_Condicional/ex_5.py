'''Elabore um programa que leia do teclado o sexo de uma pessoa. Se o sexo
digitado for "M" ou "m" ou "F" ou "f", escrever na tela "Sexo válido!". Caso contrário,
exibir "Sexo inválido!".'''

#Variáveis
sexo = input("Digite o sexo de uma pessoa:")

if (sexo == "M" or sexo == "m" or sexo == "F" or sexo == "f"):
    print("Sexo válido!")

else:
    print("Sexo inválido!")
