#Cenário:

#A equipe de auditoria do seu banco/empresa recebeu a string contendo as informações brutas do bilhete aéreo enviado no PDF. Você precisa criar um script em Python para extrair e validar os dados da transação

# O que seu código deve fazer:

# Fazer o parsing (divisão) dessa string e extrair os valores para variáveis adequadas (converter valores numéricos para float).

# Recalcular o valor total somando: VALOR_VOO + TAXAS + BAGAGEM.

# Criar uma estrutura condicional (if/else) para verificar se o PAGO na string é igual ao valor total recalculado pelo seu código:

# Se for igual, imprima: "✅ Conciliação Aprovada: O valor total de R$ [Valor] confere."

# Se houver divergência, imprima: "❌ Alerta de Divergência: Valor pago não confere com a soma dos itens."

# Formatar a saída de todos os valores monetários com duas casas decimais usando f-strings.

dados_bilhete = "COD:QRGYOE;PASSAGEIRO:Assunção Domingos ;VALOR_VOO:495.00;TAXAS:40.46;BAGAGEM:130.00;PAGO:665.46"

# Fazer o parsing (divisão) dessa string e extrair os valores para variáveis adequadas
valores = dados_bilhete.split(";")
cod = valores[0].split(":")[1]
passageiro = valores[1].split(":")[1]
valor_voo = float(valores[2].split(":")[1])
taxas = float(valores[3].split(":")[1])
bagagem = float(valores[4].split(":")[1])
pago = float(valores[5].split(":")[1])

# Recalcular o valor total
valor_total = valor_voo + taxas + bagagem

# Verificar conciliação
if pago == valor_total:
    print(f"✅ Conciliação Aprovada: O valor total de R$ {valor_total:.2f} confere.")
else:
    print(f"❌ Alerta de Divergência: Valor pago não confere com a soma dos itens.")