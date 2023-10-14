'''Faça um programa, utilizando funções, que retorne o valor de um produto já com o imposto. Deverão ser
utilizado dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
porcentagem e custo, que é o custo de um item antes do imposto.
Para este exercício crie três funções:
    • entrada() - serve para retornar tanto o custo do produto quanto a porcentagem do imposto;
    • somaImposto(porc, custo) - recebe o valor da porcentagem do imposto e o custo do produto.
    Retorna o novo custo do produto já com o imposto.
    • main() - chamada das funções criadas (chama 2 vezes a entrada e 1 vez a função somaImposto)
    e depois mostre o custo com o imposto.'''

#Funções
def entrada(texto):
    valor = float(input(texto))    
    return valor
    

def somaImposto(porc, custo):
    novoPreco = custo + (custo * porc/100)
    return novoPreco


def main():
    custo = entrada("Digite o valor do produto: ")
    porc = entrada("Digite o valor da porcentagem do imposto: ")

    result = somaImposto(porc, custo)
    print(f"O valor do produto com o imposto é de: {result:.2f}")


main()
