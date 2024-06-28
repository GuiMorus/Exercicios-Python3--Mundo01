# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 5% de aumento

# Variável resgatando o salário do funcionário
salario = float(input("Qual o seu salário bruto R$"))

# Mostrando o aumento salarial
print("Um salário de R${:.2f} com aumento de 5%, seu novo salário será R${:.2f}".format(salario, salario * 1.05))
