# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
# separados em unidade, dezena, centena e milhar

# Variável resgatando o valor digitado
num = str(input("Digite um valor entre 0 e 9999: ")).zfill(4)

# Mostrando os dígitos separados
print(f"Unidade: {num[3]}")
print(f"Dezena: {num[2]}")
print(f"Centena: {num[1]}")
print(f"Milhar: {num[0]}")
