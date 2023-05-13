from jogo import *
from time import sleep
from random import randint


def linha():
    print('-=' * 30)


def encerramento():
    print('\nEncerrando...')
    sleep(1)
    print('Programa encerrado!')


player1 = player2 = oponente = nome = jogada = nome_jogador_da_vez = escolha_jogador_da_vez = x_ou_o = ''

jogo_interrompido = False

linha()
print('[1] Contra a máquina [2] Dois Jogadores '.center(60))
linha()

tabuleiro = JogoDaVelha()

jogadores_ou_maquina = 0
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
        jogo_interrompido = True
        break


if jogadores_ou_maquina == 1 and not jogo_interrompido:

    while True:
        try:
            nome = str(input(f'Seu nome: ')).title().strip()

            if nome != '':
                break
            print('Digite um nome válido!')
        except KeyboardInterrupt:
            encerramento()
            jogo_interrompido = True
            break

    player1 = Jogador(nome=nome, escolha='x')
    oponente = Maquina(escolha='o')

if jogadores_ou_maquina == 2 and not jogo_interrompido:

    jogadores_criados = 1
    while True:
        try:

            if jogadores_criados == 1:

                nome = str(input(f'Nome do jogador {jogadores_criados}: ')).title().strip()
                player1 = Jogador(nome=nome, escolha='x')
                jogadores_criados += 1

            if jogadores_criados == 2:

                nome = str(input(f'Nome do jogador {jogadores_criados}: ')).title().strip()
                player2 = Jogador(nome=nome, escolha='o')
                break

        except KeyboardInterrupt:
            encerramento()
            jogo_interrompido = True
            break

    quem_comeca = randint(1, 2)
    if quem_comeca == 1:
        nome_jogador_da_vez = player1.nome
        escolha_jogador_da_vez = player1.escolha

    if quem_comeca == 2:
        nome_jogador_da_vez = player2.nome
        escolha_jogador_da_vez = player2.escolha

if not jogo_interrompido:
    while True:
        tabuleiro.representacao_tabuleiro()

        while True:

            try:

                jogada = str(input(f'Sua vez {nome_jogador_da_vez} ({escolha_jogador_da_vez}): ')).strip().upper()

                if jogada in tabuleiro.tabuleiro.keys():
                    break
                print('Escolha uma opção válida')
            except KeyboardInterrupt:
                encerramento()
                jogo_interrompido = True
                break

        if jogo_interrompido:
            break

        if nome_jogador_da_vez == player1.nome:
            tabuleiro.joga(jogada, player1.escolha)

            nome_jogador_da_vez = player2.nome
            escolha_jogador_da_vez = player2.escolha
            continue

        if nome_jogador_da_vez == player2.nome:
            tabuleiro.joga(jogada, player2.escolha)

            nome_jogador_da_vez = player1.nome
            escolha_jogador_da_vez = player1.escolha
