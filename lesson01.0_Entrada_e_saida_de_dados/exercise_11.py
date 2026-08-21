# 11) Ler do teclado um número inteiro e imprimir seu sucessor e antecessor. Para tal, utilizar o print com vírgulas.
# Exemplo:
# Entrada:
# Digite um número inteiro: 11
# Saída:
# Sucessor: 12
# Antecessor: 10

# Entrada de dados
numero = int(input("Digite um número inteiro: "))
# Cálculo do sucessor e antecessor
sucessor = numero + 1
antecessor = numero - 1
# Saída de dados
print("Sucessor:", sucessor)
print("Antecessor:", antecessor)