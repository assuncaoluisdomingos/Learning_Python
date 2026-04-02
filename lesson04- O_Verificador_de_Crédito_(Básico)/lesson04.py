# Entrada de Dados com a interação do usuário
salario = float(input("Digite o salário mensal: R$ "))
parcela = float(input("Digite o valor da parcela desejada: R$ "))

# Lógica de Negócio (O que o Analista de Dados faz)
limite_maximo = salario * 0.30

print(f"\n--- Relatório de Análise Financeira ---")
print(f"Seu limite de parcela é: R$ {limite_maximo:.2f}")

# Tomada de Decisão (Condicional if/else) para a aprovação do emprestimo 
if parcela <= limite_maximo:
    print("STATUS: Empréstimo APROVADO. ✅")
else:
    print("STATUS: Empréstimo NEGADO. Risco de inadimplência alto. ❌")