from random import randint
from funcoes import *

nomes = list()
nom = continua = ''
elementos_historia = dict()
qtd_nom = 0

while True:
    nom = str(input('Nome qualquer (pode ser de um personagem fictício): ')).strip().capitalize()
    if nom in nomes:
        print(cores('vermelho', 'Erro!!'), 'Esse ja foi.')
    elif nom not in nomes:
        nomes.append(nom)
        qtd_nom += 1
    if qtd_nom == 4:
        while True:
            continua = str(input('Quer adicionar mais algum nome? [S/N] ')).strip().upper()[0]
            if continua == 'N':
                break
            print(cores('vermelho', 'Erro!!'), 'Escolha uma opção válida!')

