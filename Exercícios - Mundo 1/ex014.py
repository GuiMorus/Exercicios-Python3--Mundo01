# Escreva um programa que converta uma temperatura de ºC para °F

# Variável resgatando a quantidade Graus Celsius
celsius = float(input("Qual é a temperatura em Celsius: "))

# Mostrando a conversão de Celsius para Fahrenheit
fah = (celsius * 9 / 5) + 32  #Fórmula de Celsius para Fahrenheit
print("Uma temperatura de {:.3f}°C equivale à {:.3f}ºF".format(celsius, fah))
