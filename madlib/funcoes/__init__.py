def len_lista(lis):
    tam = len(lis)
    return tam


def cores(cor, msg):
    c = {'fechar': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m',
         'magenta': '\033[35m', 'ciano': '\033[36m'}
    return f'{c[f"{cor}"]}{msg}{c["fechar"]}'
