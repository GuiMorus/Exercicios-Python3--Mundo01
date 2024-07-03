# Faça um programa que lia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.

# Variável resgatando o nome completo do usuário
nome = str(input("Digite seu nome completo: ").strip())
nome = nome.split()     # Listando o nome
ultimo = len(nome) - 1  # Resgatando último valor da tabela

# Mostrando o primeiro e último nome
print(f"Seu primeiro nome é: {nome[0].title()}")
print(f"Seu último nome é: {nome[ultimo].title()}")
# OUTRA FORMA
# print(f"Seu último nome é: {nome[-1].title()}")
# Nota: utilizando o -1 o Python pega o ultimo valor da lista
# assim como o -2 pega o penultimo item da lista
