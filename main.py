lista_de_tarefas = list()
contador = 1


def menu():
    print('------------------------')
    print('Menu:')
    print('1 Adicionar uma Tarefa')
    print('2 Remover uma Tarafa')
    print('3 Exibir Tarefas')
    print('4 Sair')


def add():
    global contador
    print(' ')
    tarefa = input('Insira um novo item ')

    lista_de_tarefas.append((contador, tarefa))
    print(' ')
    print(f'a tarefa {tarefa} foi inserida com sucesso')
    contador += 1


def undo():
    print(' ')
    numero_da_tarefa = int(input('Qual tarefa deseja Remover '))
    for tarefa in lista_de_tarefas:
        if tarefa[0] == numero_da_tarefa:
            lista_de_tarefas.remove(tarefa)
            print(' ')
            print(f'A tarefa {tarefa} foi removida com sucesso')
        else:
            print(' ')
            print('nenhuma tarefa encotrada')


def display():
    if not lista_de_tarefas:
        print(' ')
        print('a lista esta vazia')
    else:
        print(' ')
        print('Lista de Tarefas')
        for tarefa in lista_de_tarefas:
            print(tarefa)


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
