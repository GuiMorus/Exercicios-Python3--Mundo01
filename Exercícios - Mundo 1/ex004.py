# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possíveis sobre ela

# Resgatando um valor e atribuindo a uma variável
variavel = input("Digite o que quiser: ")

# Descrevendo informações sobre o valor resgatado e mostrando no print()
print("Tipo Primitívo: ", type(variavel))                       # verifica o tipo do valor
print("Numérico: {}".format(variavel.isnumeric()))              # verifica se é numérico
print("Decimal: {}".format(variavel.isdecimal()))               # verifica se é decimal
print("Alfanumérico: {}".format(variavel.isalnum()))            # verifica se tem número e letras
print("Alfabético: {}".format(variavel.isalpha()))              # verifica se tem só letras
print("Capitalizado: {}".format(variavel.istitle()))            # verifica se está capitalizado
print("Letras Minúsculas: {}".format(variavel.islower()))       # verifica se tudo é minúsculo
print("Letras Maiúsculas: {}".format(variavel.isupper()))       # verifica se tudo é maiúsculo
