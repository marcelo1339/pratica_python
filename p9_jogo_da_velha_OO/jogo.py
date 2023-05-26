class JogoDaVelha:
    def __init__(self):
        self.__tabuleiro = {'A1': '', 'A2': '', 'A3': '',
                            'B1': '', 'B2': '', 'B3': '',
                            'C1': '', 'C2': '', 'C3': ''}

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    def representacao_tabuleiro(self):

        print('    A     |    B    |    C')

        print(f'1    {self.__tabuleiro["A1"].center(1)}    |    {self.__tabuleiro["B1"].center(1)}    |    '
              f'{self.__tabuleiro["C1"].center(1)}')

        print(f'2    {self.__tabuleiro["A2"].center(1)}    |    {self.__tabuleiro["B2"].center(1)}    |    '
              f'{self.__tabuleiro["C2"]}')

        print(f'3    {self.__tabuleiro["A3"].center(1)}    |    {self.__tabuleiro["B3"].center(1)}    |    '
              f'{self.__tabuleiro["C3"].center(1)}')

    def joga(self, coluna_e_linha, x_ou_o):
        if self.__tabuleiro[coluna_e_linha] == '':
            self.__tabuleiro[coluna_e_linha] = x_ou_o

    def fim_de_jogo(self):
        tabuleiro = self.__tabuleiro

        # busca vertical
        colunas = ['A', 'B', 'C']
        for coluna in colunas:

            indice_coluna = 1

            if tabuleiro[f'{coluna}{indice_coluna}'] == tabuleiro[f'{coluna}{indice_coluna + 1}'] == \
                    tabuleiro[f'{coluna}{indice_coluna + 2}'] != '':

                return True, tabuleiro[f'{coluna}{indice_coluna}']

        # busca horizontal
        for indice_linha in range(1, 4):

            if tabuleiro[f'A{indice_linha}'] == tabuleiro[f'B{indice_linha}'] == tabuleiro[f'C{indice_linha}'] != '':
                return True, tabuleiro[f'A{indice_linha}']

        # busca diagonal
        if tabuleiro['A1'] == tabuleiro['B2'] == tabuleiro['C3'] != '':

            return True, tabuleiro['A1']

        elif tabuleiro['C1'] == tabuleiro['B2'] == tabuleiro['A3'] != '':

            return True, tabuleiro['C1']


class Jogador:
    def __init__(self, nome, escolha):
        self.__nome = nome
        self.__escolha = escolha.upper()

    def __str__(self):
        return f'Nome: {self.__nome}. Escolha: {self.__escolha}'

    @property
    def escolha(self):
        return self.__escolha

    @property
    def nome(self):
        return self.__nome
