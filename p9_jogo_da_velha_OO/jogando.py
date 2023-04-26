from jogo import *
from time import sleep
from random import randint


def linha():
    print('-=' * 30)


def encerramento():
    print('\nEncerrando...')
    sleep(1)
    print('Programa encerrado!')


jogadores_ou_maquina = 0

jogadores_criados = 1

player1 = player2 = oponente = nome = jogada = ''

quem_comeca = randint(1, 2)

linha()
print('[1] Contra a máquina [2] Dois Jogadores '.center(60))
linha()

tabuleiro = JogoDaVelha()

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
    player1 = Jogador(nome=nome, escolha='x')
    oponente = Maquina(escolha='o')
elif jogadores_ou_maquina == 2:
    while True:
        try:
            nome = str(input(f'Nome do jogador {jogadores_criados}')).title()
        except KeyboardInterrupt:
            encerramento()
            break

        if jogadores_criados == 1:
            player1 = Jogador(nome=nome, escolha='x')
            jogadores_criados += 1
            continue

        if jogadores_criados == 2:
            player2 = Jogador(nome=nome, escolha='o')
            break

if quem_comeca == 1:
    vez_do_jogador = player1.nome
elif quem_comeca == 2:
    vez_do_jogador = player2.nome

while True:
    tabuleiro.representacao_tabuleiro()
    print(tabuleiro.tabuleiro)

    while True:
        try:
            jogada = str(input('Sua vez {}: '))

            if jogada in tabuleiro.tabuleiro.keys():
                break
            print('Escolha uma opção válida')

        except KeyboardInterrupt:
            encerramento()
            break
    break
