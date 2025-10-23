# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5', '6.5']
cont = 0
total = 0
while cont < len(notas): 
    total = float(notas[cont]) + total
    cont = cont + 1
    media = total / len(notas)
print(f'{media:.2f}')




# LOOP FOR
total = 0
for nota in notas: 
    total = total + float(nota)
media = total / len(notas)
print(f'{media:.2f}')
