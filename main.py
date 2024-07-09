n = list()

def mostra(text):
    print(f"{text} ")

def menu():
    mostra('Menu:')
    mostra('1 Adicionar uma Tarefa')
    mostra('2 Remover uma Tarafa')
    mostra('3 Exibir Tarefas')
    mostra('4 Sair')


def add():
    t = input('Insira um novo item')

    n.append(t)
    mostra(f'a tarefa {t} foi inserida com sucesso')


def undo():
    t = input('Qual tarefa deseja Remover')
    if t in n:
        n.remove(t)
        mostra(f'A tarefa {t} foi removida com sucesso')
    else:
        mostra('nenhuma tarefa encotrada')
def display():
    if not n:
        mostra('a lista esta vazia')
    else:
        mostra('Lista de Tarefas')
        for t in n:
            mostra(t)
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
        mostra('Saindo...')
        break
    else:
        mostra('a opcao escolhida e ivalida ou inesxitente ')