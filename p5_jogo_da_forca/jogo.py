"""Todas as palavras que estão no arquivo -palavras.txt- foram retiradas do perfil Python Pro:
https://github.com/pythonprobr/palavras"""

from p5_jogo_da_forca.funcoes import *
from time import sleep


cabeca = tronco = perna_esq = perna_dir = braco_esq = braco_dir = olhos = nariz = boca = interrompe = False
palavras = set()
usu = str()
word = menos_palavras(palavras, 'palavras.txt')


while True:
    if (cabeca and tronco and perna_esq and perna_dir and braco_esq and braco_dir and olhos and nariz and boca) \
            or interrompe:
        break


    linha()
    print('Jogo da forca'.center(60))
    linha()

    while True:
        try:
            linha()
            print(f'A palavra tem {len(word)} letras.')
            usu = str(input('Tente uma letra: ')).strip().upper()[0]
        except (ValueError, TypeError, IndexError):
            print('Por favor, tente uma letra!')
        except KeyboardInterrupt:
            print('\nEncerrando...')
            interrompe = True
            print('Programa encerrado')
            break



"""(primeiro a cabeça, depois o tronco, de seguida pernas e braços e termina-se com olhos, nariz e boca)"""
