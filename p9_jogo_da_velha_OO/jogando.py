from jogo import *
from time import sleep
from random import randint


def linha():
    print('-=' * 30)


def encerramento():
    print('\nEncerrando...')
    sleep(1)
    print('Programa encerrado!')


player1 = player2 = nome = jogada = nome_jogador_da_vez = escolha_jogador_da_vez = ''

jogo_interrompido = False

tabuleiro = JogoDaVelha()


jogadores_criados = 1
while True:
    try:

        if jogadores_criados == 1:

            while True:
                nome = str(input(f'Nome do jogador {jogadores_criados}: ')).title().strip()

                if nome != '':
                    player1 = Jogador(nome=nome, escolha='x')
                    jogadores_criados += 1
                    break
                print('Digite um nome válido!')

        if jogadores_criados == 2:

            while True:
                nome = str(input(f'Nome do jogador {jogadores_criados}: ')).title().strip()

                if nome != '':
                    player2 = Jogador(nome=nome, escolha='o')
                    jogadores_criados += 1
                    break
                print('Digite um nome válido!')

    except KeyboardInterrupt:
        encerramento()
        jogo_interrompido = True
        break

    break

quem_comeca = randint(1, 2)
if quem_comeca == 1:
    nome_jogador_da_vez = player1.nome
    escolha_jogador_da_vez = player1.escolha

if quem_comeca == 2:
    nome_jogador_da_vez = player2.nome
    escolha_jogador_da_vez = player2.escolha

print('\nA jogada deve ser a união entre os índices de coluna e célula (A1, A2, ...)')

if not jogo_interrompido:
    while True:

        linha()
        tabuleiro.representacao_tabuleiro()
        linha()

        if tabuleiro.fim_de_jogo():

            escolha_jogador_vencedor_ou_empate = tabuleiro.fim_de_jogo()[1]

            if escolha_jogador_vencedor_ou_empate == 'X':
                print(f'Parabéns, {player1.nome}!! Você venceu.')
            elif escolha_jogador_vencedor_ou_empate == 'O':
                print(f'Parabéns, {player2.nome}!! Você venceu.')
            elif escolha_jogador_vencedor_ou_empate == 'EMPATE':
                print('Parece que houve um empate!!')

            break

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
