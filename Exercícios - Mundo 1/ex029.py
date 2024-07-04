# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado, a multa vai
# custar R$7,00 por cada Km acima do limite

# Variável resgatando a velocidade do veículo
velocidade = float(input("Qual a velocidade do seu carro(Km/h): "))

# Verificando se é passível de multa
limite = 80
multa = velocidade - 80

if velocidade > 80:
    print("⚠ Você está acima da velocidade ⚠")
    print(f"Você pagará uma multa de R${multa * 7:.2f}")
else:
    print("Tenha uma boa viagem")
