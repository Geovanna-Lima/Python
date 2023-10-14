'''Faça um programa, utilizando funções, que receba três números inteiros e positivos, e que forneça a
soma desses três números.
Para este exercício crie três funções:
    • entrada() - retorna um número digitado (fazer a verificação se é positivo);
    • calculaSoma(a, b, c) - recebe 3 números inteiros e positivos e retorna a soma deles;
    • main() - chamada das funções criadas (chama 3 vezes a entrada, sendo uma para cada número e a
    função para somar) e depois mostre o resultado.'''

#Funções
def entrada():
    num = int(input("Digite um número: "))

    while num <= 0:
        num = int(input("Número inválido! \nDigite um número: "))

    return num


def calculaSoma(a, b, c):
    result = a + b + c
    return result


def main():
    a = entrada()
    b = entrada()
    c = entrada()

    soma = calculaSoma(a, b, c)
    print(f'O resultado da soma é: {soma:.2f}')


main()
