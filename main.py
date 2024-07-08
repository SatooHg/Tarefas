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
