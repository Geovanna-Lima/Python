'''Elabore um programa que receba o preço de etiqueta de um produto e calcule e mostre o quanto
deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de
pagamento.
Utilize os códigos da tabela seguinte para ler qual a condição de pagamento escolhida e efetuar o cálculo
adequado.
    Código Condições de pagamento
      1    À vista em dinheiro ou cheque, recebe 10% de desconto
      2    À vista no cartão de crédito, recebe 5% de desconto
      3    Em 2 vezes, preço normal de etiqueta sem juros
      4    Em 3 vezes, preço normal de etiqueta mais juros de 10%'''

#Variáveis
preco = float(input("Digite o valor da etiqueta do produto adquirido:"))

#Opção escolhida
print("Como deseja pagar? \n 1 - À vista em dinheiro ou cheque, recebe 10% de desconto \n 2 - À vista no cartão de crédito, recebe 5% de desconto \n 3 - Em 2 vezes, preço normal de etiqueta sem juros \n 4 - Em 3 vezes, preço normal de etiqueta mais juros de 10%")
forma_pagamento = int(input("Digite a forma de pagamento:"))

#Elif
if (forma_pagamento == 1):
    total = preco - (preco * 0.10)
    print(f"O valor total à vista em dinheiro é de: R$ {total:.2f}")
    
elif (forma_pagamento == 2):
    total = preco - (preco * 0.05)
    print(f"O valor total à vista no cartão de crédito é de: R$ {total:.2f}")

elif (forma_pagamento == 3):
    print(f"O valor total parcelado em 2X é de: R$ {preco:.2f}")
    print(f"O valor que será pago em cada parcela será de: R$ {(preco/2):.2f}")

elif (forma_pagamento == 4):
    total = preco + (preco * 0.10)
    print(f"O valor total parcelado em 3X é de: R$ {total:.2f}")
    print(f"O valor que será pago em cada parcela será de: R$ {(total/3):.2f}")

else:
    print("Valor inválido!")
