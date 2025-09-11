modelo = input('qual foi o modelo de carro que você alugou ?')
km = float(input('quantos km foram rodados ?'))
dias = float(input('quantos dias você ficou com o carro ?'))

if modelo == 'fusca':
    diaria = 199
elif modelo == 'carro de golfe':
    diaria = 387
elif modelo == 'fox':
    diaria = 10
else:
    diaria = 60

custo_dias = dias * diaria
custo_km = km * 0.15 
valor_total = custo_dias + custo_km

print(f"você alugou um {modelo} e ficou com ele por {dias} dias e andou {km} km com ele, sendo assim você vai pagar R${valor_total}")
 