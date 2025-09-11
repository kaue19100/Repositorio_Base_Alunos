# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('escolha uma das opções abaixo:')
print('1. dollar para real')
print('2. real para dollar')
opcao = input('qual foi a opção escolhida ?' )

if opcao == '1':
    cotacao_dollar = float(input('qual a atual cotação do dollar ?'))
    dollar = float(input('quantos dollares você quer converter para real ? '))
    resultado_1 = dollar * cotacao_dollar
    print(f'você tem {dollar:.2f} dollares, ao converter para real vc tera {resultado_1:.2f}R$')
elif opcao == '2':
    cotacao_dollar = float(input('qual a atual cotação do dollar ?'))
    real = float(input('quantos R$ você quer concverter pra dollar ?'))
    resultado_2 = (real / cotacao_dollar)
    print(f'com {real:.2f}R$ você consegue {resultado_2:.2f} dollares. Um absurdo né ? ')

else:
    print('digite apenas o numero 1 ou 2.')