from random import choice


def gerar_senha(qtd_senhas, qtd_caracteres):

    caracteres_disponiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                              '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
                              '^', '_', '`', '{', '|', '}', '~']

    senha_atual = list()
    senhas = dict()


    for c in range(0, qtd_senhas):
        for caractere in range(0, qtd_caracteres):
            senha_atual.append(choice(caracteres_disponiveis))

        if senha_atual not in senhas.values():
            senhas[f'senha{c}'] = senha_atual[:]
            senha_atual.clear()

    s = ''
    for pos, c in enumerate(senhas.values()):
        for caractere in c:
            s += f'{caractere}'
            if len(s) == len(c):
                break

    print(s)
    return senhas


if __name__ == '__main__':
    print(gerar_senha(3, 5))
