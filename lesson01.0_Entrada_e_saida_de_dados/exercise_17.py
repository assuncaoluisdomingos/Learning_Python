# 17) Criar um algoritmo que, a partir da leitura de dois valores inteiros (base e altura), calcule e imprima a área de um triângulo. A área de um triângulo equivale à metade do valor da multiplicação da sua base pela sua altura (base * altura / 2). A resposta não deverá possuir dígitos decimais. Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Digite o valor da base (em metros): 10
# Digite o valor da altura (em metros): 23
# Saída:
# Área do triângulo: 115 metros quadrados

# Entrada de dados
base = int(input("Digite o valor da base (em metros): "))
altura = int(input("Digite o valor da altura (em metros): "))

# Cálculo da área
area = base * altura // 2

# Saída de dados
print(f"Área do triângulo: {area} metros quadrados")