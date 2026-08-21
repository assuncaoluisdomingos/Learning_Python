# 22) Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das Vendas por eles efetuadas.
# Escreva um algoritmo que leia o número de carros negociados por determinado vendedor, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor, com duas casas decimais. Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Quantos carros foram vendidos no mês? 15
# Qual foi o valor total das vendas (em reais)? 750000
# Qual é o salário fixo do vendedor (em reais)? 3000
# Qual é o valor fixo que o vendedor recebe por cada carro vendido (em reais)? 850
# Saída:
# Neste mês, o vendedor irá receber R$ 53250.00.

# Entrada de dados
num_carros_vendidos = int(input("Quantos carros foram vendidos no mês? "))
valor_total_vendas = float(input("Qual foi o valor total das vendas (em reais)? "))
salario_fixo = float(input("Qual é o salário fixo do vendedor (em reais)? "))
valor_por_carro = float(input("Qual é o valor fixo que o vendedor recebe por cada carro vendido (em reais)? "))

# Cálculo do salário final
comissao_carros = num_carros_vendidos * valor_por_carro
bonus_vendas = valor_total_vendas * 0.05
salario_final = salario_fixo + comissao_carros + bonus_vendas

# Saída de dados
print(f"Neste mês, o vendedor irá receber R$ {salario_final:.2f}.")
