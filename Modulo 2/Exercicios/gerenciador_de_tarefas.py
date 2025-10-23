import os
tarefas = {
    "tarefas": ['Estudar', 'Pegar fc Chanpions 20 ⭐'],
    "datas": ["17/10 Até 06/11", "17/10 Até 20/10"]
}
def mostrar_tarefas():
    barra = f'| {60* '-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefas: {tarefas['tarefas'] [i] } | Datas: {tarefas ['datas'] [i]}')
    input('Aperte ENTER para continuar...')

def adicionar_tarefas():
    barra = f'| {60* '-'}|'
    print(barra)
    tarefa = input('Adicione a tarefa:    ')
    data = input('Coloque a data em que a tarefa tem que ser cumprida:    ' )
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)
    print('Tarefa adicionada com sucesso !!!')

    print('Adicionar tarefas')
    input('Aperte ENTER para continuar...')
def remover_tarefas():
    barra = f'| {60* '-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefas: {tarefas['tarefas'] [i] } | Datas: {tarefas ['datas'] [i]}') 
    id_tarefa = int(input('| Digite o número da tarefa que deseja remover:   '))
    if id_tarefa > 0: 
        tarefa = tarefas['| tarefas'].pop(id_tarefa - 1)
        tarefas['| datas'].pop(id_tarefa - 1)
    else: 
        print('| ID invalido ')
    print(f'| tarefa "{tarefa}" removida com sucesso !!!')
    print(barra)
    input('| Aperte ENTER para continuar...')
    print('| Remover tarefas')
    input('| Aperte ENTER para continuar...')

def menu():
    while True: 
        try:
            os.system('cls')
            barra = f'| {60* '-'}|'
            print(barra)
            print('|GERENCIADOR DE TAREFAS')
            print(barra)
            print('| 1 - Mostrar tarefas')
            print('| 2 - Adicionar tarefas')
            print('| 3 - Remover tarefas ')
            print('| 4 - Sair')
            print(barra)
            opc = int(input('|Escolha uma opção:   '))
            if opc == 1:
                os.system('cls')
                mostrar_tarefas()
            elif opc == 2:
                os.system('cls')
                adicionar_tarefas()
            elif opc == 3:
                os.system('cls')
                remover_tarefas()
            elif opc == 4:
                print('|Saindo do programa..... ')
                break
            else:
                os.system('cls')
                print('|Opção invalida')
                input('|Aperte ENTER para continuar...')
        except: 
            print('ERRO digite uma opção valida !!!   ')
            input('|Aperte ENTER para continuar...')
menu()