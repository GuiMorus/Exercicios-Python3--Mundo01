# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto

from datetime import date

# Variável resgatando o ano
ano = int(input("Digite um ano para saber se é bissexto: "))

# Se for digitado 0 pegará o ano atual
if ano == 0:
    ano = date.today().year

# Verificando se o ano é bissexto
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")
