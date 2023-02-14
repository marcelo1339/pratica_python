from random import randint, choice


def palavra_txt(origem_txt):
    """
    A ideia é diminuir uma grande quantidade de palavras de um txt.
    >>precisa das funções 'choice' e 'randint' do módulo 'random' para funcionar.<<

    :param origem_txt: Recebe o arquivo de texto que contêm a lista de palavras
    :return: retorna a palavra que vai ser usada
    """

    print('Aguarde! Sua palavra está sendo selecionada...')

    s = set()
    palavra = str()
    novas_palavras = list()
    cont = aleatorio = 0
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for letra in alfabeto:
        with open(origem_txt, 'r', encoding='utf-8') as plv:
            for p in plv:
                cont = 0
                aleatorio = randint(0, 1)
                if (p.upper()[0] == letra) and ('-' not in p) and ('.' not in p) and (' ' not in p) and (aleatorio == 1) \
                        and len(p) > 4 and (cont <= 1000):
                    s.add(p.lower())
                    cont += 1

    for p in s:
        novas_palavras.append(p)

    palavra = choice(novas_palavras)
    return palavra


def linha():
    print('-=' * 30)
