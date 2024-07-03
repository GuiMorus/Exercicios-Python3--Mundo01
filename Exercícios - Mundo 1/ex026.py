# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra A
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

# Variável resgatando a frase
frase = str(input("Digite uma frase: ").strip())
frase = frase.lower()     # Tratando informação
frase = frase.replace(" ", "")      # Tratando informação

# Mostrando a quantidade e posições do A
print(f"A letra 'A' apareceu {frase.count('a')} vezes,")
print(f"A primeira vez que ela aparece é na {frase.find('a') + 1}° posição,")
print(f"A ultima vez que ela aparece é na {frase.rfind('a') + 1}° posição.")
