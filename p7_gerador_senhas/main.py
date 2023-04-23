"""Eu não recomendo o uso desse programa para gerar senhas que serão efetivamente usadas no
seu dia a dia. Isso porquê, eu apenas o criei para praticar programação."""

from random import choice
from time import sleep


def gerar_senha(qtd_senhas, qtd_caracteres):

    caracteres_disponiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                              '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
                              '^', '_', '`', '{', '|', '}', '~']
    senhas = dict()

    for s in range(0, qtd_senhas):
        senha_atual = ''

        for caractere in range(0, qtd_caracteres):
            escolha = choice(caracteres_disponiveis)
            senha_atual += escolha

        if senha_atual not in senhas.values():
            senhas[f'senha{s}'] = senha_atual

    for p, senha in enumerate(senhas.values()):
        print(f'senha{p+1}: {senha}')
        sleep(0.5)


if __name__ == '__main__':
    (gerar_senha(12, 11))
