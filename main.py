n = list()


def menu():
    print('Mene:')
    print('1 Adicionar uma Tarefa')
    print('2 Remover uma Tarafa')
    print('3 Exibir Tarefas')
    print('4 Sair')


def add():
    t = input('Insira um novo intem')
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
    if not n
        print('a lista esta vazia')
    else:
        print('Lista de Tarefas')
        for t in n
            print(t)