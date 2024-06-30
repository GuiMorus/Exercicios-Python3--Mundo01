# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

# Variáveis recolhendo os nomes dos alunos
alunos = input("Nome dos 4° estudante separados vírgula: ").title()  # .title() para corrigir a capitalização
lista = alunos.split(", ")  # .split() para separar os nomes pelas vírgulas e espaços

# Mostrando a lista sorteada entre os alunos
shuffle(lista)  # Embaralhando a lista
print(f"A ordem de apresentação será: \n{lista}")
