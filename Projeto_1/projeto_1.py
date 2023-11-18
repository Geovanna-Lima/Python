# Nome: Geovanna da Silva Lima | TIA: 32383193
# Nome: Isadora Caetano Brandão de Sousa | TIA: 32396058

# Cores
vermelho = '\033[31m'
original = '\033[0;0m'
negrito = '\033[1m'
verde = '\033[32m'

# Categorias cadastradas
categorias = {'A': 'Alimentos', 'T': 'Transporte', 'M': 'Moradia', 'S': 'Saúde', 'E': 'Entretenimento'}

# Armazenamento inicial de limite e despesa
limites = {'A': 0, 'T': 0, 'M': 0, 'S': 0, 'E': 0}
despesas = {'A': 0, 'T': 0, 'M': 0, 'S': 0, 'E': 0}

# Ver se todos os limites foram cadastrados
todos_limites_cadastrados = False


# Função Menu
def exibir_menu():
    print(negrito, "\nSISTEMA DE CONTROLE DE ORÇAMENTO", original)
    print("1. Cadastrar categorias e limites")
    print("2. Cadastrar despesa diária")
    print("3. Exibir resumo e estatísticas")
    print("4. Finalizar programa")


# Função Categoria e Limite
def cadastrar_categoria_limite():
    global todos_limites_cadastrados  # Usar a variável global

    if todos_limites_cadastrados:
        print(vermelho, "TODOS OS LIMITES JÁ FORAM CADASTRADOS!", original)
        return

    print(negrito, "\nSISTEMA DE CONTROLE DE ORÇAMENTO – CATEGORIAS E LIMITES:", original)

    for chave, valor in categorias.items():
        print(f"{chave}: {valor}")

    categoria = input("\nESCOLHA A CATEGORIA (A/T/M/S/E) PARA DEFINIR O LIMITE: ").upper()

    if categoria in categorias:
        if limites[categoria] == 0:
            try:
                limite = float(input("Insira o limite de orçamento: R$"))

                if limite < 0:
                    print(vermelho, "O LIMITE DEVE SER POSITIVO!", original)

                else:
                    limites[categoria] = limite
                    print(f"O Limite de R${limite:.2f} foi definido para a categoria {categorias[categoria]}")

            except ValueError:
                print(vermelho, "LIMITE INVÁLIDO, INSIRA UM NÚMERO VÁLIDO!", original)

        else:
            print(vermelho, "LIMITE JÁ CADASTRADO PARA ESTA CATEGORIA!", original)

    else:
        print(vermelho, "CATEGORIA INVÁLIDA!", original)

    # Verificar se todos os limites foram cadastrados
    todos_limites_cadastrados = all(limites.values())


# Função Despesa Diária
def cadastrar_despesa():
    global todos_limites_cadastrados

    if not todos_limites_cadastrados:
        print(vermelho, "VOCÊ DEVE DEFINIR LIMITES PARA TODAS AS CATEGORIAS ANTES DE REGISTRAR DESPESAS!", original)
        return

    print(negrito, "\nSISTEMA DE CONTROLE DE ORÇAMENTO – DESPESA DIÁRIA:", original)

    for chave, valor in categorias.items():
        print(f"{chave}: {valor}")

    categoria = input("\nEscolha uma categoria (A/T/M/S/E): ").upper()

    if categoria in categorias:
        try:
            valor = float(input("Insira o valor da despesa: R$"))
            if valor < 0:
                print(vermelho, "O VALOR DEVE SER POSITIVO!", original)

            else:
                despesas[categoria] += valor
                print(f"Despesa de R${valor:.2f} registrada na categoria {categorias[categoria]}.")

        except ValueError:
            print(vermelho, "VALOR INVÁLIDO, INSIRA UM NÚMERO VÁLIDO.", original)

    else:
        print(vermelho, "CATEGORIA INVÁLIDA!", original)


# Função Resumo
def exibir_resumo():
    if not todos_limites_cadastrados:
        print(vermelho, "VOCÊ DEVE CADASTRAR OS LIMITES PRIMEIRO!", original)
        return

    print(negrito, "\nSISTEMA DE CONTROLE DE ORÇAMENTO – RESUMO", original)

    for categoria in categorias:
        print(f"{categorias[categoria]}:")
        print(f"- Despesa: R${despesas[categoria]:.2f}")
        print(f"- Limite de Orçamento: R${limites[categoria]:.2f}")

        if despesas[categoria] > limites[categoria]:
            print(vermelho, "Limite excedido\n", original)

        else:
            print(verde, "Não excedido\n", original)

    print(negrito, "SISTEMA DE CONTROLE DE ORÇAMENTO – ESTATÍSTICAS", original)

    total_gasto = sum(despesas.values())
    print(f"- Total de Gasto: R${total_gasto:.2f}")

    diferenca_desplim = sum(despesas.values()) - sum(limites.values())
    print(f"- Total da diferença entre as despesas e os limites: R${diferenca_desplim:.2f}")

    divisao_limites = sum(limites.values()) // 5
    print(f"- Média dos limites: R${divisao_limites:.2f}")


# Chamada das funções
while True:
    exibir_menu()
    opcao = input("\nESCOLHA UMA OPÇÃO (1/2/3/4): ")

    if opcao == '1':
        cadastrar_categoria_limite()

    elif opcao == '2':
        cadastrar_despesa()

    elif opcao == '3':
        exibir_resumo()

    elif opcao == '4':
        print(negrito, "\nSISTEMA DE CONTROLE DE ORÇAMENTO – SOBRE", original)
        print("Este programa foi desenvolvido por:\n- Geovanna da Silva Lima \n- Isadora Caetano Brandão de Sousa")
        print(negrito, "ENCERRANDO O PROGRAMA")
        break

    else:
        print(vermelho, "OPÇÃO INVÁLIDA, TENTE NOVAMENTE!", original)
