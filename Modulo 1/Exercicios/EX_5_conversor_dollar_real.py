# Escreva um programa que pede ao usuário o valor atual da cotação do dollar e a quantidade de dólares para ser convertido em reais. 
# Depois mostre na tela a conversão.

# OUTPUT ESPERADO:

# Digite a cotação do dollar: 5.60
# Digite o valor em dollar a ser convetido para real: 100
# O valor em reais é:  560.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dollar = float(input('quantos dollares você quer converter ?'))
cotacao = float(input('qual a cotação atual do dollar ?'))
reais = dollar * cotacao

print(f'ao converter você ficara com {reais} R$')

