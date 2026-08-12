#Este programa vai ler a hora e os minutos separadamete e calcular o total de minutos que se passaram desde o incio do dia.Como demostro do código abaixo, o programa vai ler a hora e os minutos separadamente, calcular o total de minutos que se passaram desde o início do dia e exibir o resultado mas fazendo uma subtração do total de horas do dia (24) com a hora digitada pelo usuário, multiplicando o resultado por 60 e somando com os minutos digitados pelo usuário.

# 1. Armazenamento dos dados (Variáveis)
horas_do_dias= 24
hora_de_entrada = int(input("Digite a hora atual (0-23): "))
minutos = int(input("Digite os minutos atuais (0-59): "))

# 2. Processamento dos dados (Cálculo do total de minutos)
hora = horas_do_dias - hora_de_entrada
total_minutos = (hora * 60) + minutos   

# 3. Exibição do resultado (Total de minutos desde o início do dia)
print(f"\n Este programa rodo as {hora} horas e {minutos} minutos representam um total de {total_minutos} minutos desde o início do dia.")