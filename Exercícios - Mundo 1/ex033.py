# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

# Variáveis recolhendo os números
num = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Variáveis do maior e menor
maior = num
menor = num2

# Verificando se o maior realmente é o maior
if menor > maior:
    maior = num2
    menor = num

# Verificando se o num3 é o menor de todos
if num3 < menor:
    menor = num3

# Verificando se o num3 é o maior de todos
if num3 > maior:
    maior = num3

print(f"maior {maior} | menor {menor}")
