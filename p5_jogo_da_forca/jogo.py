"""Todas as palavras que estão no arquivo -palavras.txt- foram retiradas do perfil Python Pro:
https://github.com/pythonprobr/palavras"""

from p5_jogo_da_forca.funcoes import *
from time import sleep


interrompe = False
usu = str()
palavra = list()
nao_existe = list()
plvs_usadas = list()
letras_repetidas = list()
word = list()
cont = c = indice_atual = 0

for l in palavra_txt('palavras.txt'):
    word.append(l.lower())

del word[-1]

for l in word:
    palavra.append('_')

while True:
    if cont == 9 or interrompe:
        break

    linha()
    print('Jogo da forca'.center(60))
    linha()

    while True:
        try:
            if cont == 9:
                print(':-( Parece que você perdeu!')
                break

            linha()

            print(word)

            print(f'--Você tem {9 - cont} tentativas.')
            print(f'--A palavra tem {len(word)} letras.')
            usu = str(input('>>Tente uma letra: ')).strip().lower()[0]

            if not usu.isalpha():
                print('Por favor, tente uma letra!')

            if usu not in word and usu.isalpha():
                if usu not in nao_existe:
                    nao_existe.append(usu)
                print(nao_existe)
                cont += 1

            if usu in word:
                indice_atual = word.index(usu, indice_atual)
                print(indice_atual)

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
