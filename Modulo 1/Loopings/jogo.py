from random import randint 
print('TENTE ADIVINHAR O NUMERO DE 1 A 1000')
corret = randint(1,1000)
numero = int(input('digite um numero qualquer.'))
while numero != (corret):
    if numero < (corret):
        numero = int(input(f'errado ! seu numero é maior que {numero} digite um novo numero.  '))
    elif numero > (corret):
        numero = int(input(f'numero errado ! é menor que {numero} digite um novo numero.  '))
print('aeeeeeeeeeeeeeeeee acertou, demora da desgraça. se vc acertou de primeira vc é um desgraçado, gastou a sorte da sua vida')
        

