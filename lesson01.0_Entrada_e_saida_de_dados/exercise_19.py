# 19) Criar um algoritmo que leia um valor real correspondente ao peso em quilos de uma pessoa. Calcular e imprimir:
# • o peso da pessoa em gramas, duas casas decimais
# • o novo peso, em quilos, se a pessoa engordar 12%
# Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Qual é o peso da pessoa (em quilos)? 65.5
# Saída:
# A pessoa em questão pesa 65500.00 gramas.
# Se ela engordar 12%, passará a pesar 73.36 quilos.

# Entrada de dados
peso_quilos = float(input("Qual é o peso da pessoa (em quilos)? "))
# Cálculo do peso em gramas e do novo peso com aumento de 12%       
peso_gramas = peso_quilos * 1000
novo_peso_quilos = peso_quilos * 1.12           

# Saída de dados
print(f"A pessoa em questão pesa {peso_gramas:.2f} gramas.")
print(f"Se ela engordar 12%, passará a pesar {novo_peso_quilos:.2f} quilos.")
