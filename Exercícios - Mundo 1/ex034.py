# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu pagamento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%. Para os inferiores(ou iguais)
# um aumento de 15%

# Variável resgatando o valor do salário
salario = float(input("Para saber o aumento, digite seu salário(em Reais): "))

# Mostrando o aumento salarial dependendo do valor
if salario > 1250:
    aumento = salario * 1.10
    print(f"Seu salário teve um aumento de 10%, agora você recebe R${aumento:.2f}")

if salario <= 1250:
    aumento = salario * 1.15
    print(f"Seu salário teve um aumento de 15%, agora você recebe R${aumento:.2f}")
