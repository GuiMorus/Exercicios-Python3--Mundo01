# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

# Variável resgatando o nome do usuário
nome = str(input("Digite seu nome completo: ").strip())

# Mostrando o nome tudo em maiúsculo e minúsculo
print(f"Seu nome em maiúsculo fica: {nome.upper()}")
print(f"Seu nome em minúsculo fica: {nome.lower()}")

# Mostrando quantas letras tem o nome todo e quantas tem o primeiro nome
nome_formatado = nome.replace(" ", "")
nome_lista = nome.split()

print(f"Ao todo seu nome tem {len(nome_formatado)} letras")
print(f"Seu primeiro nome tem {len(nome_lista[0])} letras")
