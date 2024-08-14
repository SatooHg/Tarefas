try:
    arquivo = open('Test.json', 'r')
    lista_de_tarefas = arquivo.read().splitlines()
    arquivo.close()
except FileNotFoundError:
    lista_de_tarefas = []


def menu():
    print('------------------------')
    print('Menu:')
    print('1 Adicionar uma Tarefa')
    print('2 Remover uma Tarafa')
    print('3 Exibir Tarefas')
    print('4 Sair')


def add():
    print(' ')
    tarefa = input('Insira um novo item: ')
    lista_de_tarefas.append(tarefa)
    arquivo = open('Test.json', 'w')
    for tarefa in lista_de_tarefas:
        arquivo.write(tarefa + '\n')
    arquivo.close()
    print(' ')
    print(f'A tarefa "{tarefa}" foi inserida com sucesso.')


def undo():
    print(' ')
    if not lista_de_tarefas:
        print('lista vazia')
        return

    numero_da_tarefa = int(input('inisira o numero da tarefa que deseja remover '))

    if numero_da_tarefa <= 0 or numero_da_tarefa > len(lista_de_tarefas):
        print('numero insirido e invalido')
        return

    removedor_de_tarefas = lista_de_tarefas.pop(numero_da_tarefa - 1)
    arquivo = open('Test.json','w')
    for tarefa in lista_de_tarefas:
        arquivo.write(tarefa + '\n')
        arquivo.close()
    print(' ')
    print(f'a tarefa {removedor_de_tarefas} foi removida com sucesso')


def display():
    if not lista_de_tarefas:
        print(' ')
        print('a lista esta vazia')
        print(' ')
    else:
        print(' ')
        print('Lista de Tarefas')
        for numero, tarefa in enumerate(lista_de_tarefas, start=1):
            print(f'{numero}. {tarefa}')


while True:
    menu()
    op = input('Escolha uma Opcao 1 2 3 ou 4 ')

    if op == '1':
        add()
    elif op == '2':
        undo()
    elif op == '3':
        display()
    elif op == '4':
        print('Salvando...')
        print('Saindo...')
        break
    else:
        print('a opcao escolhida e ivalida ou inesxitente ')
