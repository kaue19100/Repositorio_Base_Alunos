# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dia = int(input('que dia é hoje ?'))

if dia == 1:
    print('hoje é domingo feira (era pra ser bom, mas é ruim)')
elif dia == 2:
    print('hoje é segunda feira (dia medilcre. horrivel !)')
elif dia == 3:
    print('hoje é terça feira (dia chato)')
elif dia == 4:
    print('hoje é quarta feira (meh)')
elif dia == 5: 
    print('hoje é quinta feira (até que é legalzinho)')
elif dia == 6:
    print('hoje é sexta feira (otimo dia)')
elif dia == 7:
    print('hoje é sabado feira (melhor dia.)')

else:
    print('numero errado')











