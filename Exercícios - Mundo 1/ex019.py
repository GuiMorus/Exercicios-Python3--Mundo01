# Um professor quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome escolhido.

from random import choice

# Variáveis recolhendo os nomes dos alunos
aluno00 = input("Nome do 1° estudante: ").title()   # .title() para corrigir a capitalização
aluno01 = input("Nome do 2° estudante: ").title()
aluno02 = input("Nome do 3° estudante: ").title()
aluno03 = input("Nome do 4° estudante: ").title()

# Mostrando o aluno sorteado
sorteado = choice([aluno00, aluno01, aluno02, aluno03])

print(f"Quem foi sorteado(a) foi {sorteado}")
