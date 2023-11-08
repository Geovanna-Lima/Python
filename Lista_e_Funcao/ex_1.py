'''Faça um programa em Python que leia duas listas – uma com peso e a outra com a altura de 15 pessoas.
Construir uma lista de mesmo tamanho com o índice de massa corporal de cada pessoa (IMC).
IMC = peso/(altura)2
UTILIZAR FUNÇÕES PARA A ENTRADA DE DADOS, PROCESSAMENTO E SAÍDA'''

peso = []
altura = []
imc = []
qnt_pessoas = 3

def entrada():
    for i in range(qnt_pessoas):
        # Pedir peso
        print(f"Digite o peso da {i + 1}ª pessoa: ")
        p =  int(input())
        peso.append(p)

        # Pedir Altura
        print(f"Digite a altura da {i + 1}ª pessoa: ")
        a =  float(input())
        altura.append(a)


def processamento():
    for i in range(qnt_pessoas):
        resp = peso[i] / (altura[i]**2)
        imc.append(resp)
        

def saida():
    for i in range(qnt_pessoas):
        print(f"{i + 1}ª pessoa: peso = {peso[i]:.1f}, altura = {altura[i]:.2f} e imc = {imc[i]:.2f}")

      
entrada()
processamento()
saida()
