altura = float(input('qual a sua altura ?'))
peso = float(input('qunatos kg você pesa ?'))
imc = peso / (altura ** 2)
print(f'seu imc é {imc: .2f}')