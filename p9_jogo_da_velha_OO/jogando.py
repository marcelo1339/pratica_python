from jogo import *
from time import sleep


def linha():
    print('-=' * 30)


def encerramento():
    print('\nEncerrando...')
    sleep(1)
    print('Programa encerrado!')


jogadores_ou_maquina = 0
nome = ''
player1 = player2 = pc = ''

linha()
print('[1] Contra a máquina [2] Dois Jogadores '.center(60))
linha()

while True:
    try:
        jogadores_ou_maquina = int(input('>> Sua escolha '))
        if jogadores_ou_maquina in (1, 2):
            break
        print('Escolha uma opção válida!')

    except ValueError:
        print('Escolha uma opção válida!')

    except KeyboardInterrupt:
        encerramento()
        break


if jogadores_ou_maquina == 1:
    pc = Maquina()
elif jogadores_ou_maquina == 2:
    while True:
        jogadores_criados = 1
        try:
            nome = str(input(f'Nome do jogador {jogadores_criados}')).title()
        except KeyboardInterrupt:
            encerramento()
            break

        if jogadores_criados == 1:
            player1 = Jogador(nome=nome)
            jogadores_criados += 1
        elif jogadores_criados == 2:
            player2 = Oponente(nome=nome)
            break

