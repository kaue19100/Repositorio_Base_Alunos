# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|----------------------------|')
print('|----------cadastro----------|')
print('|----------------------------|')
nome = input('| qual o seu nome ?   |')
idade = int(input(f'|quantos anos você tem {nome} ?|'))
gmail = input('|qual o seu gmail ?  |')
senha = input('| digite a senha do seu gmail|')

print('|----------------------------|')
print('|-----CADASTRO COMCLUIDO-----|')
print(f'|seja bem vindo(a) {nome}!  |')
print(f'| gmail: {gmail}            |')
print('|----------------------------|')