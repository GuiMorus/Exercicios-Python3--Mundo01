# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

# Variável resgatando o valor do produto
valor = float(input("Qual o valor do produto? R$"))

# Mostrando o desconto do produto
desconto = valor - (valor * 0.05)
print("Seu produto de R${:.2f} com desconto de 5% fica R${:.2f}".format(valor, desconto))
