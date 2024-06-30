# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa
# Fórmula: a² + b² c²
# Em que: a² = cateto oposto | b² = cateto adjacente | c² = hipotenusa

from math import hypot

# Variáveis resgatando os valores dos catetos
oposto = float(input("Digite o comprimento do Cateto Oposto: "))
adjacente = float(input("Digite o comprimento do Cateto Adjacente: "))

# Mostrando o calculo da hipotenusa
hipo = hypot(oposto, adjacente)
print(f"Hipotenusa: {hipo:.2f}")
