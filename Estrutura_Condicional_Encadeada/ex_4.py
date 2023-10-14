'''Faça um programa que tendo como dados de entrada o código de região de localização do cliente,
o nome do cliente, o número de peças vendidas e o nome do vendedor; calcule e informe o valor do
frete, a comissão do vendedor e o lucro obtido com a venda, sabendo-se que:
    - O valor do frete depende da quantidade transportada e da região;
    - Custo por peça = R$ 7,00;
    - Custo total = custo por peça * número de peças vendidas;
    - Valor total da venda = custo total acrescido de 50%;
    - Comissão do vendedor = 6,5 % do valor total da venda;
    - Lucro = Valor total venda – custo total – comissão do vendedor;
    
Valor do Frete por Região:
Código da Região  |  Nome da Região  |  Valor do frete por peça (até 1.000 peças)  |  R$ Valor do frete por peça(acima de 1.000 peças)R$
       1          |       Sul        |               1,00                          |                        0,9
       2          |      Norte       |               1,10                          |                        1,0
       3          |      Leste       |               1,15                          |                        1,10
       4          |      Oeste       |               1,20                          |                        1,15'''

print("\nCódigo das regiões: \n1 - Sul \n2 - Norte \n3 - Leste \n4 - Oeste")

regiao = int(input("Entre com o código da regiao: "))
cliente = input("Entre com o nome do cliente: ")
quant = int(input("Entre com a quantidade de peças vendidas: "))
vendedor = input("Entre com o nome do vendedor: ")

frete = 0

if quant <= 1000 and regiao == 1:
    frete = quant*1.00
elif quant > 1000 and regiao == 1:
    frete = quant*0.9
elif quant <= 1000 and regiao == 2:
    frete = quant*1.10
elif quant > 1000 and regiao == 2:
    frete = quant*1.0
elif quant <= 1000 and regiao == 3:
    frete = quant*1.15
elif quant > 1000 and regiao == 3:
    frete = quant*1.10
elif quant <= 1000 and regiao == 4:
    frete = quant*1.20
elif quant > 1000 and regiao == 4:
    frete = quant*1.15

custoTotal = 7.00*quant
valorTotalVenda = custoTotal*1.5
comissao = valorTotalVenda*0.065
lucro = valorTotalVenda - custoTotal - comissao

print("\nINFORMAÇÕES PEDIDAS")
print("Frete..................R$", frete)
print("Comissão do vendedor...R$", comissao)
print("Lucro..................R$", lucro)

