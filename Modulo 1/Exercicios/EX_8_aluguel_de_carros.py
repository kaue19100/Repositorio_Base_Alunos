# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

km = float(input('quantos km foram rodados com o carro ?'))
dias = int(input('quantos dias você ficou com o carro ?'))

km_total = km * 0.15
dias_totais = dias * 60
aluguel_total = km_total + dias_totais
print(f'Você ficou com o seu carro por {dias} dias e rodou {km} km. O total a pagar é {aluguel_total}R$')
