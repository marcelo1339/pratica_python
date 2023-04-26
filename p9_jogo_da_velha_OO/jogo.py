class JogoDaVelha:
    def __init__(self):
        self.__tabuleiro = {'A1': '', 'A2': '', 'A3': '',
                            'B1': '', 'B2': '', 'B3': '',
                            'C1': '', 'C2': '', 'C3': ''}

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    def representacao_tabuleiro(self):
        print('    A    |    B   |    C')
        print(f'1    {self.__tabuleiro["A1"]}    |    {self.__tabuleiro["A2"]}    |    {self.__tabuleiro["A3"]}')
        print(f'2    {self.__tabuleiro["B1"]}    |    {self.__tabuleiro["B2"]}    |    {self.__tabuleiro["B3"]}')
        print(f'3    {self.__tabuleiro["C1"]}    |    {self.__tabuleiro["C2"]}    |    {self.__tabuleiro["C3"]}')

    def joga(self, coluna_e_linha, x_ou_o):
        self.__tabuleiro[coluna_e_linha] = x_ou_o


class Jogador:
    def __init__(self, nome, escolha):
        self._nome = nome
        self._escolha = escolha

    def __str__(self):
        return f'Nome: {self.nome}. Escolha: {self._escolha}'

    @property
    def escolha(self):
        return self._escolha

    @property
    def nome(self):
        return self.nome


class Maquina:
    def __init__(self, escolha):
        self.nome = 'Máquina'
        self._escolha = escolha

    @property
    def escolha(self):
        return self._escolha


# tabuleiro = JogoDaVelha()
# tabuleiro.representacao_tabuleiro()
