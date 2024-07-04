# Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar

# Variável resgatando o número
num = int(input("Digite um número: "))

# Verificando se é par ou ímpar
if num % 2 == 0:
    print(f"{num} é um número par")
else:
    print(f"{num} é um número ímpar")
