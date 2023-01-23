def formatacao(fmt, msg):
    s = str(fmt).lower()
    fechar = '\033[m'

    c = {'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'azul': '\033[34m',
         'magenta': '\033[35m', 'ciano': '\033[36m'}
    f = {'padrão': '\033[0m', 'negrito': '\033[1m', 'sublinhado': '\033[4m', 'negativo': '\033[7m'}

    if s in c.keys():
        return f'{c[f"{s}"]}{msg}{fechar}'
    elif s in f.keys():
        return f'{f[f"{s}"]}{msg}{fechar}'


def linha():
    print('-=' * 40)

