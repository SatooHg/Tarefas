n = list()

def add():
    t = input('Insira um novo intem ')
    t = input('Insira um novo item')

    n.append(t)
    print(f'a tarefa {t} foi inserida com sucesso ')
    print(f'a tarefa {t} foi inserida com sucesso')


def undo():
    t = input('Qual tarefa deseja Remover ')
    t = input('Qual tarefa deseja Remover')
    if t in n:
        n.remove(t)
        print(f'A tarefa {t} foi removida com sucesso ')
        print(f'A tarefa {t} foi removida com sucesso')
    else:
        print('nenhuma tarefa encotrada ')
        print('nenhuma tarefa encotrada')
def display():
    if not n:
        print('a lista esta vazia ')
        print('a lista esta vazia')
    else:
        print('Lista de Tarefas')
        for t in n: