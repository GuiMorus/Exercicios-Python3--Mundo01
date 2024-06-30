# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua
# porção inteira

from math import trunc

# Variável resgatando o valor
num = float(input("Digite um número: "))

# Mostrando os números retirados após a vírgula do valor
print(f"O número {num} tem sua porção inteira {trunc(num)}")
