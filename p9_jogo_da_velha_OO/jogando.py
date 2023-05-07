from jogo import *
from time import sleep
from random import randint


def linha():
    print('-=' * 30)


def encerramento():
    print('\nEncerrando...')
    sleep(1)
    print('Programa encerrado!')


player1 = player2 = oponente = nome = jogada = vez_do_jogador = x_ou_o = ''
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
            nome = str(input(f'Nome do jogador {jogadores_criados}: ')).title().strip()
        except KeyboardInterrupt:
            encerramento()
            jogo_interrompido = True
            break

        if jogadores_criados == 1:
            player1 = Jogador(nome=nome, escolha='x')
            jogadores_criados += 1

        if jogadores_criados == 2:
            player2 = Jogador(nome=nome, escolha='o')
            jogadores_criados += 1

        if jogadores_criados == 3:
            break

    quem_comeca = randint(1, 2)
    if quem_comeca == 1:
        vez_do_jogador = player1.nome

    if quem_comeca == 2:
        vez_do_jogador = player2.nome

if jogadores_ou_maquina in (1, 2) and not jogo_interrompido:
    while True:
        tabuleiro.representacao_tabuleiro()
        print(tabuleiro.tabuleiro)

        while True:
            try:
                jogada = str(input(f'Sua vez {vez_do_jogador}: ')).strip().upper()

                if jogada in tabuleiro.tabuleiro.keys():
                    break
                print('Escolha uma opção válida')
            except KeyboardInterrupt:
                encerramento()
                jogo_interrompido = True
                break

        if jogo_interrompido:
            break

        if vez_do_jogador == player1.nome:
            tabuleiro.joga(jogada, player1.escolha)
            vez_do_jogador = player2.nome

        if vez_do_jogador == player2.nome:
            tabuleiro.joga(jogada, player2.escolha)
            vez_do_jogador = player1.nome
