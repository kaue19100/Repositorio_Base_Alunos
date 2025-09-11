dias = int(input("quantos dias você ficou com o carro?"))
km = float(input('quantos km você andou com o carro ?'))
total_dias = dias * 60
total_km = km * 0.15
print(f'você ficou incriveis {dias} dias com o carro, e rodou surpreendentes {km}km. Sendo assim o total a pagar somando tudo é r${total_dias + total_km}')