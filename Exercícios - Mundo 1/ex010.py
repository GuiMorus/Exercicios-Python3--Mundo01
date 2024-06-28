# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Considere US$1,00 = R$3,27

# Variável resgatando o valor em Reais via input()
real = float(input("Manda a braba, tem quantas verdinhas ae? R$"))

# Mostrando a conversão de Reais em Dólares via print()
print("Com essa grana aê cê pode comprar US${:.2f} doletas".format(real / 3.27))
