idade = int(input('quantos anos você tem ?'))
carteira = input('você possui carteira de motorista ? (s/n)')
print(f'você pode dirigir ? {idade >= 18 and carteira == 's' }')