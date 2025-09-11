# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

carro = input('qual o carro que você comprou ?')
valor = float(input(f'qual o preço do {carro} coprado ?'))
desconto = int(input('qual a porcentagem de desconto que você recebeu ?'))

valor_desconto = valor * (desconto / 100)

valor_total = valor - valor_desconto

print(f'Você comprou um {carro} pelo preço de {valor}R$ aplicando {desconto} de desconto você pagara {valor_total}R$ pelo seu {carro}')

