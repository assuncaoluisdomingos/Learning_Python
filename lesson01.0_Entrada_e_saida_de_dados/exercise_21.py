# 21) Escreva um algoritmo que leia o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores, com duas casas decimais. Para tal, utilizar o print com vírgulas.
# Exemplo:
# Entrada:
# Qual é o número total de eleitores do município? 5000
# Qual é o número total de votos válidos? 3722
# Quantas pessoas votaram em branco? 573
# Quantas pessoas votaram nulo? 705
# Saída:
# Percentual de votos válidos: 74.44 %
# Percentual de votos em branco: 11.46 %
# Percentual de votos nulos: 14.10 %

# Entrada de dados
total_eleitores = int(input("Qual é o número total de eleitores do município? "))   
votos_validos = int(input("Qual é o número total de votos válidos? "))
votos_branco = int(input("Quantas pessoas votaram em branco? "))
votos_nulo = int(input("Quantas pessoas votaram nulo? "))

# Cálculo dos percentuais
percentual_validos = (votos_validos / total_eleitores) * 100
percentual_branco = (votos_branco / total_eleitores) * 100
percentual_nulo = (votos_nulo / total_eleitores) * 100

# Saída de dados
print(f"Percentual de votos válidos: {percentual_validos:.2f} %")
print(f"Percentual de votos em branco: {percentual_branco:.2f} %")
print(f"Percentual de votos nulos: {percentual_nulo:.2f} %")
