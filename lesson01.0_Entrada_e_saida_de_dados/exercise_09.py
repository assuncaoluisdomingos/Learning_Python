# 9) Crie um algoritmo que leia dois números inteiros do teclado. Execute a adição entre eles e imprima-os no formato mostrado abaixo, com um caractere que representa o <enter> embutido na resposta. Para tal, utilizar um único print com vírgulas.
# Exemplo:
# Entrada:
# Digite um número inteiro: 40
# Digite outro número inteiro: 15
# Saída:
# ### Resultado da Operação ###
# 40 + 15 = 55

# Entrada de dados
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
# Adição
resultado = numero1 + numero2
# Saída de dados
print("### Resultado da Operação ###\n", numero1, "+", numero2, "=", resultado) 