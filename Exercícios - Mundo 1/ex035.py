# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles
# podem ou não formar um triângulo.

# Variáveis resgatando o valor dos segmentos
a = float(input("Digite o tamanho do 1° segmento: "))
b = float(input("Digite o tamanho do 2° segmento: "))
c = float(input("Digite o tamanho do 3° segmento: "))

segmentos = [a, b, c]           # Criando lista com os valores
segmentos = sorted(segmentos)   # Reorganizando lista do menor para o maior

# Mostrando se é possível fazer um triângulo
if segmentos[2] < segmentos[0] + segmentos[1]:
    print("É possível formar um triângulo com estes lados")
else:
    print("Os lados não possuem as condições necessárias para formar um triângulo")
