lista_de_tarefas = list()


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
    tarefa = input('Qual tarefa deseja Remover ')
    if tarefa in lista_de_tarefas:
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