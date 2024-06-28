# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e em milímetros

# Váriável resgatando o valor de metros via input()
metro = float(input("Digite a quantidade de Metro: "))

# Mostrando a conversão em centímetros e milímetros via print()
print("{} Metros tem".format(metro))
print("Centímetros: ", (metro) * 100)
print("Milímetros: ", (metro) * 1000)
