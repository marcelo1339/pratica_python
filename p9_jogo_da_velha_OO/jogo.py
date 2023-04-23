class JogoDaVelha:
    def __init__(self):
        self.__tabuleiro = {'A1': '', 'A2': '', 'A3': '',
                            'B1': '', 'B2': '', 'B3': '',
                            'C1': '', 'C2': '', 'C3': ''}

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    @tabuleiro.setter
    def tabuleiro(self, coluna_e_linha):
        self.__tabuleiro[coluna_e_linha] = 'x'


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self._escolha = 'X'

    @property
    def escolha(self):
        return self._escolha


class Oponente(Jogador):
    def __init__(self, nome):
        super().__init__(nome=nome)
        self._escolha = 'O'


class Maquina:
    def __init__(self):
        pass
