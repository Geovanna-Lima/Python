#Variáveis
peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:"))

imc = peso/(altura*altura)

print(f"O seu IMC (índice de massa corporal) é: {imc:.2f}")
