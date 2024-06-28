# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado

# Variáveis resgatando os dias e quilômetros rodados pelo carro
dias = int(input("Por quantos dias o carro foi alugado: "))
km = float(input("Quantos Quilômetros(Km) foram rodados com o carro: "))

# Mostrando o calculo do aluguel do carro
aluguel = (dias * 60) + (km * 0.15)
print("{0} Garagem do Tio Rodinhas {0}".format("=" * 12))
print("Carro: Fiat Uno")
print("Dias Alugados: {} dias".format(dias))
print("Km corridos: {}Km".format(km))
print("Aluguel: R${:.2f}".format(aluguel))
print("=" * 49)
