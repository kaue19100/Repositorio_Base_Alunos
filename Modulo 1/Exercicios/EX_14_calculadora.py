# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print('|______________________________________________|')
print('|________________CALCULADORA___________________|')
print('|______________________________________________|')
print('|escolha uma das opções seguintes:             |')
opcao = int(input('|1 - soma. 2 - sbtração. 3 - multiplicação. 4 - divisão.|'))


if opcao == 1: 
    num_1 = float(input('|qual o primeiro numero quie você quer somar ?|'))
    num_2 = float(input('|qual o segundo numero ?|'))
    resultado = num_1 + num_2 
    print(f'||o resultado da soma dos numeros {num_1} e {num_2} é {resultado:.2f}.|')
elif opcao == 2:
    numero_1 = float(input('|qual o primeiro numero que voê quer subtrair ?|'))
    numero_2 = float(input('|e qual é o segundo numero da subtração ?|'))
    resultado = numero_1 - numero_2
    print(f'|o resultado da subtração entre {numero_1} e {numero_2} é {resultado:.2f}|')
elif opcao == 3:
    num_1 = float(input('|qual o primeiro numero da multiplicação ?|'))
    num_2 = float(input('|e qual é o segundo numero que você quer multiplicar ?|'))
    resultado = num_1 * num_2 
    print(f'|o resultado da multiplicação entre os numeros {num_1} e {num_2} é {resultado:.2f}|')
elif opcao == 4:
    num_1 = float(input('|qual o primeiro numero da sua divisão ?|'))
    num_2 = float(input('|e qual é o segundo numero que você quer dividir ?|'))
    resultado = num_1 / num_2
    print(f'|o resultado da divisão entre os numeros {num_1} e {num_2} é {resultado:.2f}|')
else:
    print('|digite uma das opções. 1, 2, 3, ou 4 !|')