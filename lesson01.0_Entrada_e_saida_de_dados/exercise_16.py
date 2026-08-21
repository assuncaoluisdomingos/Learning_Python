# 16) Ler dois valores inteiros distintos e armazená-los nas variáveis var1 e var2. Com o auxílio de uma variável temporária, efetue uma troca de valores entre as duas variáveis, de maneira que a variável var1 passe a ter o valor da variável var2 e vice-versa. Apresentar os valores antes e depois da troca para cada variável. As respostas deverão possuir um número total de 10 caracteres, sendo 4 dígitos decimais (depois do ponto), completando com ZERO o que faltar.
# Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Digite o valor de var1: 20
# Digite o valor de var2: 50
# Saída:
# Valor de var1 antes da troca: 00020.0000
# Valor de var2 antes da troca: 00050.0000
# Valor de var1 DEPOIS da troca: 00050.0000
# Valor de var2 DEPOIS da troca: 00020.0000

# Entrada de dados
var1 = int(input("Digite o valor de var1: "))    
var2 = int(input("Digite o valor de var2: "))    
# Saída de dados antes da troca
print(f"Valor de var1 antes da troca: {var1:010.4f}")
print(f"Valor de var2 antes da troca: {var2:010.4f}")
# Troca de valores
temp = var1
var1 = var2
var2 = temp
# Saída de dados depois da troca
print(f"Valor de var1 DEPOIS da troca: {var1:010.4f}")
print(f"Valor de var2 DEPOIS da troca: {var2:010.4f}")  