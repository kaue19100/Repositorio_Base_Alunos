# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista


# LOOP WHILE
add = int(input('quantos filmes você quer adicionar ? '))
quant = len(filmes)


while quant < add:

    filme = input('adicione um filme: ')
    filmes.append(filme)
    quant = quant +1 
print(filmes)

#LOOP FOR

add = int(input('quantos filmes você quer adicionar ? '))
quant = len(filmes)
for filme in range(quant, add ):
    filme = input('adicione um filme:  '  )
    filmes.append(filme)
print(filmes)
    




