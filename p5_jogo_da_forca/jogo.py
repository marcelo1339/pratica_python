"""Todas as palavras que estão no arquivo -palavras.txt- foram retiradas do perfil Python Pro:
https://github.com/pythonprobr/palavras"""

from p5_jogo_da_forca.funcoes import *
from time import sleep


interrompe = False
usu = str()
palavra = list()
nao_existe = list()
word = list()
indice_letra_repetida = list()
cont = c = repetidas = letras_repetidas = 0

for l in palavra_txt('palavras.txt'):
    word.append(l.lower())

del word[-1]

for l in word:
    palavra.append('_')

while True:
    if cont == 9 or interrompe:
        break

    while True:
        try:
            if cont == 9:
                print(':-( Parece que você perdeu!')
                break

            linha()
            print('Jogo da forca'.center(60))
            linha()

            print(word)

            print(f'--Você tem {9 - cont} tentativas.')
            print(f'--A palavra tem {len(word)} letras.')
            print('--Lembre-se que a palavra pode ter letras com acentos \n como "í, é, â, õ" entre outras.')

            linha()
            usu = str(input('>>Tente uma letra: ')).strip().lower()[0]

            if not usu.isalpha():
                print('Por favor, tente uma letra!')

            if usu not in word and usu.isalpha():
                if usu not in nao_existe:
                    nao_existe.append(usu)
                print(f'Suas tentativas: {nao_existe}')
                cont += 1

            if usu in word:
                repetidas = word.count(usu)
                if repetidas > 1:
                    for pos, letra in enumerate(word):
                        if (usu == letra) and (pos not in indice_letra_repetida):
                            indice_letra_repetida.append(pos)

                    for letra in word:
                        for indice in indice_letra_repetida:
                            if usu == letra:
                                palavra.pop(indice)
                                palavra.insert(indice, usu)
                    indice_letra_repetida.clear()

            print('Sua palavra: ', end='')
            for elemento in palavra:
                print(elemento, end='')
            print()

        except (ValueError, TypeError, IndexError) as erro:
            print('Por favor, tente uma letra!')
            print(f'Seu erro foi {erro}')
        except KeyboardInterrupt:
            print('\nEncerrando...')
            sleep(1)
            interrompe = True
            print('Programa encerrado')
            break
