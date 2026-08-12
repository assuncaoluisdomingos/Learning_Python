# 7) Crie um algoritmo que leia uma palavra, um número inteiro e um número real do teclado. O programa deverá também subtrair o número real do número inteiro. A seguir, imprima-os no formato mostrado abaixo, com frases explicativas. Para tal, utilizar o print com vírgulas.
# Exemplo:
# Entrada:
# Digite uma palavra: nuvem
# Digite um número inteiro: 8
# Digite um número real: 17.437
# Saída:
# A palavra digitada foi: nuvem
# Quando subtraímos o número real do inteiro, obtemos: -9.437000000000001

# Entrada de dados
palavra = input("Digite uma palavra: ")
numero_inteiro = int(input("Digite um número inteiro: "))
numero_real = float(input("Digite um número real: "))
# Subtração
resultado = numero_inteiro - numero_real
# Saída de dados
print(f"A palavra digitada foi: {palavra}")
print(f"Quando subtraímos o número real do inteiro, obtemos: {resultado}"   )