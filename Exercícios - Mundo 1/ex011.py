# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

# Variáveis resgatando a altura e largura via input()
print("Calcularei a quantidade de tinta necessária para sua parede")

largura = float(input("Qaul a largura da parede: "))
altura = float(input("Qual a altura da parede: "))
area = largura * altura     #A = b x h

# Mostrando a quantidade de tinta necessária em litros via print()
tinta = area / 2
print("Você precisará de {0:.2f} litros de tinta para pintar {1:.2f}m² de parede".format(tinta, area))
