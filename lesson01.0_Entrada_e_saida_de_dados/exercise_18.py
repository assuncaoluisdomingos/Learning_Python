# 18) Fazer um algoritmo que leia o valor do salário mínimo e o valor do salário de determinada pessoa. Calcular e imprimir quantos salários mínimos esta pessoa ganha. Mostrar o resultado com três dígitos decimais. Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Qual é o valor do salário mínimo (em reais)? 998.00
# Qual é o salário da pessoa (em reais)? 4567.89
# Saída:
# A pessoa em questão ganha 4.577 salários mínimos.

# Entrada de dados
salario_minimo = float(input("Qual é o valor do salário mínimo (em reais)? "))
salario_pessoa = float(input("Qual é o salário da pessoa (em reais)? "))
# Cálculo do número de salários mínimos
num_salarios_minimos = salario_pessoa / salario_minimo
# Saída de dados
print(f"A pessoa em questão ganha {num_salarios_minimos:.3f} salários mínimos.")
