# Utilize um loop while e um loop for para contar de 0 até o número que o usuário digitar:

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# LOOP WHILE

conta = 1

numero = int(input('Digite um numero. '))

while conta <= numero:

    print(f'numero: {conta}' )
    conta = conta +1

# LOOP FOR

numero = int(input('Digite um numero. '))

for numero in range(1, numero+1):
    print(f'{numero}')
