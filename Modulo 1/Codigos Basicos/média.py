from colorama import init, Fore
init(autoreset=True)

print('|____________________________________________________________|')
print('|           SISTEMA DE PROVAS                                |')
print('|____________________________________________________________|')
nome = input('| qual o nome do aluno ?')
nota1 = float(input('|qual foi a sua nota na primeira prova ?|'))
nota2 = float(input('|qual foi sua nota na segunda prova?|'))
media = (nota1 + nota2)/2
print('|____________________________________________________________|')
if media >= 6:
    print(Fore.GREEN+f'| CATAPINBAS VOCÊ CONSEGUIU, parabens {nome} !!! sua media é {media}|')
elif media == 5:
    print(Fore.LIGHTMAGENTA_EX+f'passou triscando !!! estude mais da proxima {nome}!!! sua media foi {media}|')
else:
    print(Fore.RED+f"| meu Deus {nome} seu pai chora no banho. REPROVADO! com uma media mediocre de {media}|")

print('|____________________________________________________________|')1