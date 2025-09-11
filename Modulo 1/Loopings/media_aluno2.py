contador = 0
notas_finais = 0
numero_p = int(input('quantas provas foram realizadas ?'))
while contador < (numero_p):

    contador = contador + 1
    nota = float(input(f'qual a nota da sua prova {contador} ?'))
    notas_finais += nota
media = notas_finais  / contador
print(f'a media da suas provas é: {media}')
 