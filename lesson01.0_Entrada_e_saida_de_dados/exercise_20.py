# 19) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. Para tal, utilizar o print com vírgulas.
# Exemplo:
# Entrada:
# Digite o componente ano da idade da pessoa: 32
# Digite o componente mês da idade da pessoa: 4
# Digite o componente dia da idade da pessoa: 27
# Saída:
# A pessoa em questão já viveu 11827 dias.

# Entrada de dados
anos = int(input("Digite o componente ano da idade da pessoa: "))
meses = int(input("Digite o componente mês da idade da pessoa: "))
dias = int(input("Digite o componente dia da idade da pessoa: "))

# Cálculo da idade em dias
idade_em_dias = anos * 365 + meses * 30 + dias

# Saída de dados
print(f"A pessoa em questão já viveu {idade_em_dias} dias.")
