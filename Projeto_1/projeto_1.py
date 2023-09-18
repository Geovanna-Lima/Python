#Variaveis
limite_alimentos = 0.0
limite_transporte = 0.0
limite_moradia = 0.0
limite_saude = 0.0
limite_entretenimento = 0.0
opcao = 0

#Função Menu
#def menu():
print("SISTEMA DE CONTROLE DE ORÇAMENTO \n (1) CADASTRAR CATEGORIAS E LIMITES \n (2) CADASTRAR DESPESA DIÁRIA \n (3) EXIBIR RESUMO E ESTATÍSTICAS \n (4) FINALIZAR PROGRAMA")
opcao = int(input("\nESCOLHA UMA OPÇÃO: "))

#Função ValidarValor

#Chamada da função "menu"
#menu()
#print(opcao)
    
#Escolhas
match opcao:
    case 1:
        print("\nSISTEMA DE CONTROLE DE ORÇAMENTO – CATEGORIAS E LIMITES \nINFORME O LIMITE DE GASTOS PARA AS CATEGORIAS:\n")
        
        limite_alimento = float(input("ALIMENTOS – R$ "))
        limite_transporte = float(input("TRANSPORTE – R$ "))
        limite_moradia = float(input("MORADIA – R$ "))
        limite_saude = float(input("SAÚDE – R$ "))
        limite_entretenimento = float(input("ENTRETENIMENTO – R$ "))

    case 2:
        print("SISTEMA DE CONTROLE DE ORÇAMENTO – DESPESA DIÁRIA")   


    case 3:
        print("SISTEMA DE CONTROLE DE ORÇAMENTO – RESUMO E ESTATÍSTICAS")

    case 4:
        print("\nSISTEMA DE CONTROLE DE ORÇAMENTO – SOBRE\n Este programa foi desenvolvido por:\n Geovanna da Silva Lima \n Isadora Caetano Brandão de Souza")

    case _:
        print("\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\n")
        #menu()
