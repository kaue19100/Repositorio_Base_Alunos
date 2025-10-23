# Calcule a média das notas utilizando loops for aninhados (um loop dentro do outro)

# O código deve exibir o resultado abaixo:

# Aluno: Fabrício | Média Final: 7.94
# Aluno: Leandro | Média Final: 8.31
# Aluno: Marcela | Média Final: 9.19


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
# Não altere e nem apague este dicionário
alunos = {
    'Fabrício' : ['9.5', '10', '6.75', '5.5'],
    'Leandro' : ['7', '8', '9.75', '8.5'],
    'Marcela' : ['9.5', '9', '9.75', '8.5'],
}
media = 0 

# LOOP FOR

for nome, notas in alunos.items():
    total = 0
    for n in notas: 
        total = total + float(n)
        media = total / len(notas)
    print(f'Aluno: {nome} | Média Final: {media:.2f} ')

