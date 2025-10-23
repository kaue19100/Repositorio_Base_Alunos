# Utilizando tanto um loop while quanto um loop for, escreva um código que exiba na tela o resultado abaixo:

#ID: 354 | Aluno: Fabrício
#ID: 847 | Aluno: Leandro
#ID: 195 | Aluno: Marcela


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
lista = ['Fabrício', 'Leandro', 'Marcela', [354, 847, 195, 0]] # Não apague e nem altere essa lista
#cont = 0

# LOOP WHILE
#hile cont <= 2:
    #print(f'ID: {lista [3] [cont]} | Aluno: {lista [cont]}  ')
    #cont = cont + 1

# LOOP FOR
for l in range(3):
    print(f'ID: {lista [3] [l]} | Aluno: {lista [l]}')
    
