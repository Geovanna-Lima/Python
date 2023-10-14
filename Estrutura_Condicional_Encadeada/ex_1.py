'''Um hospital precisa de um programa para calcular e imprimir os gastos de um paciente.
A tabela de preços do hospital é a seguinte:
- Quartos:
    - o particular – R$ 360,00
    - o semi-particular – R$ 210,00
    - o coletivo – R$ 185,00
- WIFI: R$ 3,00
- TV a cabo: R$ 4,00

Escreva um programa que leia:
    - o número de dias gastos no hospital;
    - o tipo de quarto;
    - se usou ou não o WIFI (Sim ou Nao);
    - se usou ou não a TV a cabo (Sim ou Nao).
    
Ao final, emita um relatório, como o exemplo, a seguir:
    Número de dias no hospital: 5
    Tipo de quarto: ........................... Particular
    Diárias: .................................. 1800,00
    WIFI: ..................................... 3,00
    TV a cabo: ................................ 4,00
    Total: .................................... 1807,00'''

#Variáveis
valorDiaria = 0
valorWifi = 0
valorTv = 0

dias = int(input("Quantos dias ficou no hospital? "))

quarto = input("Qual quarto: particular, semi-particular ou coletivo? ").lower()
if quarto == "particular":
    valorDiaria = dias * 360
elif quarto == "semi-particular":
    valorDiaria = dias * 210
elif quarto == "coletivo":
    valorDiaria = dias * 185
else:
    print("Tipo de quarto inválido!")
    
wifi = input("Utilizou wifi? Sim ou Nao? ").lower()
if wifi == "sim":
    valorWifi = 3
else:
    valorWifi = 0
    
tv = input("Utilizou TV? Sim ou Nao? ").lower()
if tv == "sim":
    valorTv = 4
else:
    valorTv = 0

valorTotal = valorDiaria + valorWifi + valorTv

if (quarto == "particular") or (quarto == "semi-particular") or (quarto == "coletivo"):
    print ("\nNúmero de dias no hospital: ...",dias)
    print ("Tipo de quarto: .............. ",quarto)
    print ("Diárias: ...................... R$", valorDiaria)
    print ("WIFI: ......................... R$", valorWifi)
    print ("TV a cabo: .................... R$", valorTv)
    print ("Total: ........................ R$", valorTotal)
