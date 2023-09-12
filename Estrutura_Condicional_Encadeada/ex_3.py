'''Elabore um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e. "Já trabalhou com a vítima?"
O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
responder Sim a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ela será classificada como "Inocente".'''

#Variáveis
cont = 0

#Perguntas
print("RESPONDA COM 'S' PARA SIM E 'N' PARA NÃO:")
pergunta1 = input("1 - Telefonou para a vítima?").upper()
pergunta2 = input("2 - Esteve no local do crime?").upper()
pergunta3 = input("3 - Mora perto da vítima?").upper()
pergunta4 = input("4 - Devia para a vítima?").upper()
pergunta5 = input("5 - Já trabalhou com a vítima?").upper()

#Respostas Pergunta
if (pergunta1 == "S"):
    cont = cont + 1

if (pergunta2 == "S"):
    cont = cont + 1

if (pergunta3 == "S"):
    cont = cont + 1

if (pergunta4 == "S"):
    cont = cont + 1
    
if (pergunta5 == "S"):
    cont = cont + 1

print(f"A quantidade de respostas respondidas com 'Sim' foram: {cont}")

#Verificação do Contador
if (cont == 2):
    print("Suspeita!")
    
elif (cont == 3 or cont == 4):
    print("Cúmplice!")

elif (cont == 5):
    print("Assassino!")

else:
   print("Inocente!") 
