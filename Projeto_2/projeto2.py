import random

'''Nomes dos Integrantes: 
- Geovanna da Silva Lima - 32383193 
- Isadora Caetano Brandão de Sousa - 32396058'''

# Variável global
tentativas_senha = 3

# Dados da conta
numero_conta = 0
nome = ""
telefone = ""
email = ""
saldo = 0
limite_credito = 0
senha = ""
historico_operacoes = []
contas_cadastradas = []
conta = {}
num_conta = 0
deposito = 0.00

# Função Menu
def menu():
    while True:
        print("\nMack Bank – Escolha uma Opção")
        print("(1) Cadastrar Conta Corrente")
        print("(2) Depositar")
        print("(3) Sacar")
        print("(4) Consultar Saldo")
        print("(5) Consultar Extrato")
        print("(6) Finalizar")

        opcao = int(input("Sua opção: "))

        if opcao == 1:
            cadastrar_conta()
        elif opcao == 2:
            depositar()
        elif opcao == 3:
            sacar()
        elif opcao == 4:
            consultar_saldo()
        elif opcao == 5:
            consultar_extrato()
        elif opcao == 6:
            finalizar()
        else:
            print("Opção inválida, escolha entre as opções de 1 a 6. \nTente novamente")


# Função verificar senha
def verificar_senha(senha_input):
    global senha
    global tentativas_senha

    if senha_input != senha:
        print("Senha incorreta.")
        tentativas_senha -= 1

        if tentativas_senha == 0:
            print("Limite de tentativas atingido. Opções 3, 4 e 5 bloqueadas.")
            return False

        print(f"Tentativas restantes: {tentativas_senha}")
        return False

    return True


# Função para Cadastrar Conta Corrente
def cadastrar_conta():
    global contas_cadastradas
    global num_conta
    global nome
    global telefone
    global email
    global saldo
    global limite_credito
    global senha

    if contas_cadastradas:
        print("Essa opção só pode ser acessada uma única vez.")
        return

    # Essa expressão gera um número aleatório
    numero_conta = random.randint(1000, 9999)
    
    # Recolhimento das informações do cliente e validação das informações
    print("\nMack Bank - Cadastro da Conta")
    print("Número da conta:", numero_conta)

    cliente = input("Nome do Cliente: ")
    if cliente == "":
        print("ERRO!!! \nO Nome não pode estar em branco.")
        return
    
    telefone = input("Telefone.......: ")
    if telefone == "": 
        print("ERRO!!! \nO Telefone não pode estar em branco.")
        return
    
    email = input("E-mail..........: ")
    if email == "":
        print("ERRO!!! \nO Email não pode estar em branco")
        return
    
    elif "@" not in email:
        print("ERRO!!! \nO Email não pode estar sem o símbolo do @")
        return
    
    elif "." not in email:
        print("ERRO!!! \nO Email não pode estar sem o símbolo de ponto final.")
        return
    
    saldo = float(input("Saldo Inicial...: R$ "))
    if saldo < 1000 or saldo is None:
        print("ERRO!!! \nO Saldo Inicial deve ser maior ou igual a R$1.000,00.")
        return
    
    limite_credito = float(input("Limite de crédito: R$ "))
    if limite_credito < 0 or limite_credito is None:
        print("ERRO!!! \nO Limite de Crédito deve ser maior ou igual a 0.")

    while True: 
        senha = input("Senha............: ")
        if len(senha) < 6:
            print('A Senha deve ter obrigatoriamente 6 caracteres.')
        else:
            repita_senha = input("Repita a Senha...: ")
            if senha != repita_senha:
                print("Erro!!! \nAs Senhas não coincidem.")
            else:
                # Lista para guardar as informações do usuário
                conta = {"numero_conta": numero_conta, "cliente": cliente, "telefone": telefone, "email": email, "saldo": saldo, "limite_credito": limite_credito, "senha": senha}
                contas_cadastradas.append(conta)
                print("Cadastro realizado!")
            break


# Função para depositar
def depositar():
    print("\nMack Bank - Depósito da Conta")
    num_conta = int(input("Informe o número da conta: "))

    # Procurar a o número da conta 
    for conta in contas_cadastradas:
        while conta["numero_conta"] == num_conta:
            print("Cliente: " + conta["cliente"])
            deposito = float(input("Valor do depósito: R$ "))

            # Atualizar o valor do saldo da conta
            if deposito > 0:
                conta["saldo"] += deposito
                historico_operacoes.append(f"Depósito: R$ {deposito:.2f}")
                print("Depósito realizado com sucesso!!!")
            else:
                print("O valor do depósito deve ser maior que zero!")
            return
        else:
            print("Número de conta inválido, por favor digite novamente.")
          

# Função para sacar
def sacar():
    global saldo
    global limite_credito
    global historico_operacoes

    print("\nMack Bank - Saque da Conta")
    num_conta = int(input("Informe o número da conta: "))

    # Procurar a o número da conta
    for conta in contas_cadastradas:
        while conta["numero_conta"] == num_conta:
            print("Cliente: " + conta["cliente"])
            senha_input = input("Informe a senha: ")

            if not verificar_senha(senha_input):
                return

            # Realiza o saque da conta
            valor_saque = float(input("Valor do saque: R$ "))

            if valor_saque <= saldo and valor_saque != 0:
                saldo -= valor_saque
                historico_operacoes.append(f"Saque: R$ {valor_saque:.2f}")
                print("Saque realizado com sucesso!")
            elif limite_credito >= valor_saque != 0:
                saldo -= valor_saque
                limite_credito -= valor_saque
                historico_operacoes.append(f"Saque: R$ {valor_saque:.2f} (Você está usando seu limite de crédito!)")
                print("Saque realizado com sucesso!")
            elif limite_credito < valor_saque != 0:
                print("Saldo insuficiente e sem limite de crédito disponível.")
            else:
                print("Valor do saque deve ser maior que zero.")
                return
        else:
            print("Número de conta inválido, por favor digite novamente.")


# Função para consultar saldo
def consultar_saldo():
    global saldo
    global limite_credito
    global tentativas_senha

    print("Mack Bank - Consulta Saldo")
    numero_conta_input = int(input("Informe o número da conta: "))

    if numero_conta_input != numero_conta:
        print("Número da conta incorreto.")
        return

    print("Nome:", nome_cliente)
    senha_input = input("Informe a senha: ")

    if not verificar_senha(senha_input):
        return

    print(f"Saldo Atual: R$ {saldo:.2f}")
    print(f"Limite de Crédito: R$ {limite_credito:.2f}")


# Função para Consultar Extrato
def consultar_extrato():
    print("Mack Bank - Extrato da Conta")
    numero_conta_input = int(input("Informe o número da conta: "))

    if numero_conta_input != numero_conta:
        print("Número da conta incorreto.")
        return

    print("Nome:", nome)
    senha_input = input("Informe a senha: ")

    if not verificar_senha(senha_input):
        return

    print(f"Limite de crédito: R$ {limite_credito:.2f}")
    print("Últimas operações:")

    for operacao in historico_operacoes:
        print(operacao)

    print(f"Saldo Atual: R$ {saldo:.2f}")

    if saldo < 0:
        print("Atenção ao seu saldo!")


# Função Finalizar
def finalizar():
    print("Mack Bank - Sobre")
    print("Este programa foi desenvolvido por \nGeovanna da Silva Lima - 32383193  \nIsadora Caetano Brandão de Sousa - 32396058")


menu()
