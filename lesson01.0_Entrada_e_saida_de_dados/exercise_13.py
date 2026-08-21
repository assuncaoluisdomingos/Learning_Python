# 13) Leia do teclado dois números inteiros e imprima a saída mostrada abaixo. Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Digite o primeiro número inteiro: 17
# Digite o segundo número inteiro: 3
# Saída:
# Dividendo: 17
# Divisor: 3
# Quociente: 5
# Resto: 2
dividendo = int(input("Digite o primeiro número inteiro: ")) 
divisor = int(input("Digite o segundo número inteiro: ")) 
# Saída de dados
quociente = dividendo // divisor
resto = dividendo % divisor
print(f"Dividendo: {dividendo}\nDivisor: {divisor}\nQuociente: {quociente}\nResto: {resto}")    
