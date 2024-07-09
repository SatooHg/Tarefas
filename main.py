n = list()


def menu():
    print('Menu:')
    print('1 Adicionar uma Tarefa')
    print('2 Remover uma Tarafa')
    print('3 Exibir Tarefas')
    print('4 Sair')


def add():
    t = input('Insira um novo item')

    n.append(t)
    print(f'a tarefa {t} foi inserida com sucesso')


def undo():
    t = input('Qual tarefa deseja Remover')
    if t in n:
        n.remove(t)
        print(f'A tarefa {t} foi removida com sucesso')
    else:
        print('nenhuma tarefa encotrada')
def display():
    if not n:
        print('a lista esta vazia')
    else:
        print('Lista de Tarefas')
        for t in n:
            print(t)
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