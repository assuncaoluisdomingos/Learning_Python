# 12) Ler do teclado nome, dados do endereço e telefone e imprimi-los, conforme mostrado no exemplo abaixo. Para tal, utilizar um único print com f-strings.
# Exemplo:
# Entrada:
# Digite o primeiro nome: Fulano
# Digite o sobrenome: de Tal da Silva
# Digite o nome da rua: Rua das Couves
# Digite o número da residência: 540
# Digite os códigos de área: +55 (99)
# Digite o número do telefone: 3333-3333
# Saída:
# Nome completo: Fulano de Tal da Silva
# Endereço: Rua das Couves, número 540
# Telefone: +55 (99) 3333-3333

# Entrada de dados
primeiro_nome = input("Digite o primeiro nome: ")
sobrenome = input("Digite o sobrenome: ")
nome_rua = input("Digite o nome da rua: ")
numero_residencia = input("Digite o número da residência: ")
codigo_area = input("Digite os códigos de área: ")
numero_telefone = input("Digite o número do telefone: ")
# Saída de dados
print(f"Nome completo: {primeiro_nome} {sobrenome}\nEndereço): {nome_rua}, número {numero_residencia}\nTelefone: {codigo_area} {numero_telefone}")