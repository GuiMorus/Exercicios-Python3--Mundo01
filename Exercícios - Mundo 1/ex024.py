# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo

# Variável resgatando o nome da cidade
cidade = str(input("Digite o nome da cidade em que nasceu: ").strip())
cidade = cidade.lower()     # Tratando a informação
cidade = cidade.split()     # Listando a informação

# Mostrando se o nome da cidade começa com santo
print(f"Cidade tem a palavra Santo? {"santo" in cidade[0]}")
