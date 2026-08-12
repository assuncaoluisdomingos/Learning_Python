# Este programa vai ler a conta de um usuário e vai exibir o valor da conta com 10% de desconto.
# 1. Armazenamento dos dados (Variáveis)

valor_conta = float(input("Digite o valor da conta: "))

# 2. Processamento dos dados (Cálculo do desconto)
desconto = valor_conta * 0.10

# 3. Exibição do resultado (Valor final com desconto)
valor_final = valor_conta - desconto

print(f"\nO valor da conta com 10% de desconto é: R$ {valor_final:.2f}")