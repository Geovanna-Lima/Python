''' Faça um programa que peça quatro notas de 4 alunos como valores reais entre 0 e 10,
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos
aprovados com média maior ou igual a 7.0. É necessário ler cada nota, validar se cada nota
está no intervalo entre 0 e 10 e inserir a média de cada aluno em um vetor, verificar e
contabilizar quantos alunos estão aprovados, imprimir as médias dos alunos e a quantidade
de alunos aprovados. '''

def entrada(n):
    nota = float(input(n))

    while nota < 0 or nota > 10:
        print("Nota inválida!")
        nota = float(input(n))

    return nota


# Bloco Principal
medias = []
num_alunos_aprovados = 0

for i in range(4):
    print("\nInsira as notas do aluno!")
    print(f"Aluno {i + 1}: ")

    n1 = entrada('Nota 1: ')
    n2 = entrada('Nota 2: ')
    n3 = entrada('Nota 3: ')
    n4 = entrada('Nota 4: ')

    media = (n1 + n2 + n3 + n4) / 4
    medias.append(media)

print("\nResultados:")

for i in range(len(medias)):    
    if medias[i] >= 7.0:
        print(f"Aluno {i + 1} está APROVADO, com a média: {medias[i]:.2f}")
        num_alunos_aprovados += 1
    else:
        print(f"Aluno {i + 1} está REPROVADO, com a média: {medias[i]:.2f}")

print("\nTotal:")
print(f"A quantidade de alunos aprovados são: {num_alunos_aprovados}")
    
    
