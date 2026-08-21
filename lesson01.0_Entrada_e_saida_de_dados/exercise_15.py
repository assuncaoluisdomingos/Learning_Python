# 15) Crie um algoritmo que leia hora e minutos separadamente e calcule o total de minutos que se passaram desde o início do dia. Além disso, imprima na tela a hora lida no formato “hh:mm”. Complete com ‘0’ (zeros) à esquerda para as horas de apenas um dígito. Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Digite as horas: 9
# Digite os minutos: 37
# Saída:
# Hora atual: 09:37
# Se passaram 577 minutos desde o início do dia.

# Entrada de dados
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
# Cálculo do total de minutos
total_minutos = horas * 60 + minutos
# Saída de dados
print(f"Hora atual: {horas:02d}:{minutos:02d}")
print(f"Se passaram {total_minutos} minutos desde o início do dia.")
