# 10) Criar um algoritmo que leia três números inteiros e imprima a média real entre eles. Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Digite um número: 8
# Digite outro número: 9
# Digite mais um número: 7
# Saída:
# A média entre os três números é: 8.0

# Entrada de dados
numero1 = int(input("Digite um número: "))  
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite mais um número: "))
# Cálculo da média
media = (numero1 + numero2 + numero3) / 3
# Saída de dados    
print(f"A média entre os três números é: {media}")