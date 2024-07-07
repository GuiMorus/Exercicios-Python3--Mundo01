# Escreva um programa que faça o computador escolher um número entre 0 e 5 e peça ao
# usuário descobrir qual o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

from random import randint

# Gerando um número aleatório entre 0 e 5
luck = randint(0, 5)
print("O sistema escolheu um número entre 0 e 5, tente adivinhar")
print(luck)

# Variável resgatando o valor digitado pelo usuário
num = int(input("Palpite: "))

# Verification se o usuário venceu ou não
if luck == num:
    print("PARABÉNS! Você acertou o número 🎉🎉🎉")
else:
    print("BIBIBIBIBI, você errou 😞")
