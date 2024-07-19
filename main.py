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
    tarefa = input('Insira um novo item ')

    lista_de_tarefas.append(tarefa)
    print(' ')
    print(f'a tarefa {tarefa} foi inserida com sucesso')


def undo():
    print(' ')
    if not lista_de_tarefas:


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
        print('Saindo...')
        break
    else:
        print('a opcao escolhida e ivalida ou inesxitente ')
