'''Considere o problema de conversão de temperatura:
Escreva um programa modularizado que permite ao usuário converter uma faixa de temperatura de
Fahrenheit para Celsius(para isso o usuário deve digitar F) e de Celsius para Fahrenheit (neste caso o usuário
deve digitar C).
Para a construção do programa você deve escrever as seguintes funções:
    • exibeMsg() - apenas exibe uma mensagem para ao usuário dizendo o que o programa faz e
    informando como deve ser a entrada de dados. Não tem parâmetro de entrada e não tem
    retorno;
    • verificaOpcao() - a função não tem parâmetro de entrada e retorna “F” ou “C” (fazer a validação
    para que o usuário só digite F ou C);
    • verificaIntervalo() - a função não tem parâmetro de entrada e retorna os valores inicial e final
    do intervalo (fazer a validação para que o valor inicial seja menor que o valor final);
    • exibeFahrenheitToCelsius(inicio, fim) – essa função recebe como entrada o intervalo de
    temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida
    para Celsius;
    • exibeCelsiusToFahrenheit(inicio, fim) – essa função recebe como entrada o intervalo de
    temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida
    para Fahrenheit'''

#Funções
def exibeMsg():
    print("O programa faz a conversão de Fahrenheit para Celsius ou de Celsius para Fahrenheit!")


def verificaOpcao():
    while True:
        opcao = input("Digite F ou C: ").upper()

        if opcao == "F" or opcao == "C":
            return opcao
        else:
            print("Opção inválida!")


def verificaIntervalo():
    while True:
        inicio = int(input("Digite o valor inicial: "))
        fim = int(input("Digite o valor final: "))

        if inicio < fim:
            return inicio, fim
        else:
            print("O valor inicial deve ser menor que o valor final.")

            
def exibeFahrenheitToCelsius(inicio, fim):
    for fahrenheit in range(inicio, fim):
        celsius = (fahrenheit - 32)/1.8
        print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")


def exibeCelsiusToFahrenheit(inicio, fim):
    for celsius in range(inicio, fim):
        fahrenheit = celsius * 1.8 + 32
        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")


#Chamada das funções
exibeMsg()

opcao = verificaOpcao()

if opcao == 'F':
    inicio, fim = verificaIntervalo()
    exibeFahrenheitToCelsius(inicio, fim)
else:
    inicio, fim = verificaIntervalo()
    exibeCelsiusToFahrenheit(inicio, fim)
