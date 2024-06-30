# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa
# Fórmula: a² + b² c²
# Em que: a² = cateto oposto | b² = cateto adjacente | c² = hipotenusa

# Variáveis recolhendo os valores dos catetos
oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente "))

# Mostrando o calculo da hipotenusa
hipo = (oposto ** 2 + adjacente ** 2) ** (1/2)
print(f"Hipotenusa: {hipo:.2f}")
