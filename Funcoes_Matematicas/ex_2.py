#Enunciado
'''Escreva um programa que lê dois valores em ponto flutuante e exiba os seguintes resultados:
a) divisão do primeiro valor pelo segundo valor, sem formatação;
b) divisão do primeiro valor pelo segundo valor, com exatamente seis dígitos depois da vírgula (para
isso utilize a função format)'''

#Variáveis
n1 = float(input('Digite o número 1:'))
n2 = float(input('Digite o número 2:'))

#Contas
result = n1/n2

#Exibição
print(f'A divisão do primeiro valor pelo segundo valor, sem formatação: {result}')
print(f'A divisão do primeiro valor pelo segundo valor, com exatamente seis dígitos depois da vírgula: {result:.6f}')

