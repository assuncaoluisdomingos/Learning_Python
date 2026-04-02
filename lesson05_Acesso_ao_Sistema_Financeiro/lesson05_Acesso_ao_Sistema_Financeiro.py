print("// Acesso ao Sistema Financeiro // Seja bem vido")
# Estas são as variáveis de entrada de dado do usuário 
nome=input("Digita o seu nome:")
cpf=input("Digita o teu CPF:")
nascimento=int(input("Digita a tua data de nascimento:"))

# Estas são as vaviáveis para os cálculo de matemáticos e processamentos operacional
ano_atual=2026
idade=ano_atual-nascimento 

#Definições das permições e saida de dados 
if idade >= 18:
    print(f" O {nome} com o {cpf} constam cadastrados na nossa base")
    print("Acesso ao Sistema Financeiro: PERMITIDO ✅")
else:
    print(f"Este nome {nome} com o {cpf} não consta cadastrado na nossa base")
    print("Acesso ao Sistema Financeiro: NEGADO ❌")
    