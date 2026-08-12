""" Cenário: Um gestor de portfólio pediu para você criar um script simples que calcule a performance de um ativo brasileiro.

Sua Tarefa: No Google Colab, escreva um código que:

Armazene o nome de uma ação da B3 (ex: "PETR4").

Armazene o preço de compra e o preço de venda atual.

Calcule o lucro/prejuízo bruto em percentual.

Armazene o valor total investido e exiba o valor final após a valorização. """

# 1. Armazenamento dos dados (Variáveis)
ticker = "PETR4"
preco_compra = (float(input('Digita o preço da compra:')))
preco_venda  = (float(input('Digita o preço da venda:')))
valor_investido = (float(input('Digita o valor investido:')))

# 2. Cálculos Financeiros
# Calcula a variação percentual (lucro ou prejuízo bruto)
lucro_prejuizo_pct = ((preco_venda - preco_compra) / preco_compra) * 100

# Calcula o montante final com base na valorização do ativo
valor_final = valor_investido * (1 + lucro_prejuizo_pct / 100)

# 3. Exibição do Relatório Profissional
print("-" * 50)
print(f"   RELATÓRIO EXECUTIVO DE PERFORMANCE: {ticker}")
print("-" * 50)
print(f"Preço de Aquisição:       R$ {preco_compra:.2f}")
print(f"Preço de Venda Atual:     R$ {preco_venda:.2f}")
print(f"Performance do Ativo:     {lucro_prejuizo_pct:.2f}%")
print(f"Capital Inicial Retido:   R$ {valor_investido:.2f}")
print(f"Valor Final Estimado:     R$ {valor_final:.2f}")
print("-" * 50)