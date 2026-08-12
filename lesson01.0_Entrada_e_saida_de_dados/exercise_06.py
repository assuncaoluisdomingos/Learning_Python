# 6) Crie um algoritmo que leia quatro palavras do teclado e as imprima na sequência mostrada abaixo, com a inclusão dos caracteres especiais \n e \t. Ao final, inclua um ponto. Para tal, utilizar o print com f-strings.
# Exemplo:
# Entrada:
# Digite a primeira palavra: Estou
# Digite a segunda palavra: programando
# Digite a terceira palavra: em
# Digite a quarta palavra: Python
# Saída:
# Estou
#    programando em Python.


# Entrada de dados
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
palavra3 = input("Digite a terceira palavra: ")
palavra4 = input("Digite a quarta palavra: ")

# Saída de dados
print(f"{palavra1}\n\t{palavra2} {palavra3} {palavra4}.")

