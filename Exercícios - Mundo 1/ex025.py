# Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome

# Variável resgatando o nome do usuário
nome = str(input("Digite seu nome completo: ").strip())
nome = nome.lower()     # Tratando a informação

# Mostrando se tem silva no nome
print(f"Tem Silva no nome? {"silva" in nome}")
