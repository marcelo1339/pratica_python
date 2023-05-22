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

        colunas = ['A', 'B', 'C']

        for coluna in colunas:

            # busca vertical
            indice_coluna = 1

            if tabuleiro[f'{coluna}{indice_coluna}'] == tabuleiro[f'{coluna}{indice_coluna + 1}'] == \
                    tabuleiro[f'{coluna}{indice_coluna + 2}'] != '':

                return True, tabuleiro[f"{coluna}{indice_coluna}"]

        # busca horizontal (A logica está errada)
        indice_linha = 1
        if tabuleiro[f'{colunas[0]}{indice_linha}'] == tabuleiro[f'{[colunas]}{indice_linha + 1}'] == \
                tabuleiro[f'{colunas[2]}{indice_linha + 2}']:
            return True, tabuleiro[f"{coluna}{indice_coluna}"]


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


t = JogoDaVelha()

# print(t.tabuleiro)
# t.representacao_tabuleiro()
