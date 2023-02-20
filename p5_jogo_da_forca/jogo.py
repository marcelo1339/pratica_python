"""Todas as palavras que estão no arquivo -palavras.txt- foram retiradas do perfil Python Pro:
https://github.com/pythonprobr/palavras"""

from p5_jogo_da_forca.funcoes import *
from time import sleep


cabeca = tronco = perna_esq = perna_dir = braco_esq = braco_dir = olhos = nariz = boca = interrompe = False
usu = str()
palavra = list()
plvs_usadas = list()
cont = c = letras_repetidas = 0
word = palavra_txt('palavras.txt')

while True:
    if (cabeca and tronco and perna_esq and perna_dir and braco_esq and braco_dir and olhos and nariz and boca) \
            or interrompe:
        break


    linha()
    print('Jogo da forca'.center(60))
    linha()

    while True:
        try:
            if cont == 9:
                print(' :-( Parece que você perdeu!')
                break

            linha()
            print(word)
            print(f'--Você tem {9 - cont} tentativas.')
            print(f'--A palavra tem {len(word)-1} letras.')
            usu = str(input('>>Tente uma letra: ')).strip().upper()[0]

            if not usu.isalpha():
                print('Por favor, tente uma letra!')

            if usu.upper() not in word.upper() and usu.isalpha():
                if usu.upper() not in plvs_usadas:
                    plvs_usadas.append(usu)
                print(plvs_usadas)
                cont += 1
            elif usu.upper() in word.upper():
                if c == 0:
                    for letra in word:
                        if usu.lower() == letra.lower():
                            palavra.append(letra.lower())
                        elif usu.lower() != letra.lower():
                            palavra.append('_')
                    c += 1
                    print(palavra)
                elif c > 0:
                    for letra in word:
                        if usu.lower() == letra.lower():
                            if palavra[word.index(letra)] == '_':
                                palavra.pop(word.index(usu, letras_repetidas, -1))
                                palavra.insert(word.index(usu, letras_repetidas, -1), letra)
                                letras_repetidas = word.index(usu)
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



"""(primeiro a cabeça, depois o tronco, de seguida pernas e braços e termina-se com olhos, nariz e boca)"""
