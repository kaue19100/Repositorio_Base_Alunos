print('|________________________________________________|')
print("|                calculadora                     |")
print('|________________________________________________|')
print("|escolha uma das opções:                         |")
print('| 1. soma                                        |')
print('| 2. subtração                                   |')
print('| 3. multiplicação                               |')
print('| 4. divisão                                     |')
conta = int(input('|qual opção voce escolhe ?           |'))
numero = float(input('|qual o primeiro numero da sua conta | ?'))
numero_2 = float(input('|qual o segundo numero da sua conta | ??'))
if conta == 1:
    resultado = numero + numero_2
    print(f'|o resultado da soma é {resultado}.         |')
elif conta == 2:
    resultado = numero - numero_2
    print(f'|oresultado da subtração é {resultado}.     |')
elif conta == 3:
    resultado = numero * numero_2 
    print(f'|o resultado da multiplicação pedida é {resultado}.|')
elif conta == 4: 
    resultado = numero / numero_2 
    print(f'|o resultado da divisão é {resultado}.      |')

