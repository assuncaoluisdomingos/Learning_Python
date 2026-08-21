# 14) Faça um algoritmo que leia do teclado o valor de uma conta de restaurante e imprima como resultado o valor acrescido de 5% de impostos e 10% de taxa de serviço, com duas casas depois da vírgula. Para tal, utilizar o print com vírgulas.
# Exemplo:
# Entrada:
# Digite o valor da conta sem taxas (em R$): 60.25
# Saída:
# Valor inicial da conta: R$ 60.25
# Impostos (5%): R$ 3.01
# Taxa de serviço (10%): R$ 6.03
# Valor final da conta: R$ 69.29

# Entrada de dados
valor_conta = float(input("Digite o valor da conta sem taxas (em R$): "))
# Cálculo dos valores
impostos = valor_conta * 0.05
taxa_servico = valor_conta * 0.10   
# Saída de dados
valor_final = valor_conta + impostos + taxa_servico
print(f"Valor inicial da conta: R$ {valor_conta:.2f}")
print(f"Impostos (5%): R$ {impostos:.2f}")
print(f"Taxa de serviço (10%): R$ {taxa_servico:.2f}")
print(f"Valor final da conta: R$ {valor_final:.2f}")    
