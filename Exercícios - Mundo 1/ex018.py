# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo

from math import sin, cos, tan, radians

# Variável recolhendo o valor do ângulo
angulo = float(input("Digite o ângulo: "))

# Mostrando o seno, cosseno e tangente do ângulo
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"Seno: {seno:.3f}")
print(f"Cosseno: {cosseno:.3f}")
print(f"Tangente: {tangente:.3f}")
