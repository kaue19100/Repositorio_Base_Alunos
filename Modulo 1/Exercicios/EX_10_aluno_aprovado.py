# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input('qual o nome do aluno ?     ')
nota_1 = float(input('qual a nota da primeira prova ?'))
nota_2 = float(input('qual a nota da segunda prova ?'))

media = (nota_1 + nota_2) / 2 

aprovado = (media>7) and (nota_1 != 0) and (nota_2 != 0)

print(f' o aluno {nome} foi aprovado ? {aprovado}')

