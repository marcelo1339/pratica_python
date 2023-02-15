"""Todas as palavras que estão no arquivo -palavras.txt- foram retiradas do perfil Python Pro:
https://github.com/pythonprobr/palavras"""

from p5_jogo_da_forca.funcoes import *
from time import sleep


cabeca = tronco = perna_esq = perna_dir = braco_esq = braco_dir = olhos = nariz = boca = interrompe = False
usu = str()
palavra = list()
plv_auxiliar = list()
plvs_usadas = list()
cont = c = 0
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
            if cabeca and tronco and perna_esq and perna_dir and braco_esq and braco_dir and olhos and nariz and boca:
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
                            palavra.append(letra)
                        elif usu.lower() != letra.lower():
                            palavra.append('_')
                    c += 1

                for elemento in palavra:


                for elemento in palavra:
                    print(elemento, end='')

                print()


            if cont == 1:
                cabeca = True
            elif cont == 2:
                tronco = True
            elif cont == 3:
                perna_esq = True
            elif cont == 4:
                perna_dir = True
            elif cont == 5:
                braco_dir = True
            elif cont == 6:
                braco_esq = True
            elif cont == 7:
                olhos = True
            elif cont == 8:
                nariz = True
            elif cont == 9:
                boca = True

        except (ValueError, TypeError, IndexError):
            print('Por favor, tente uma letra!')
        except KeyboardInterrupt:
            print('\nEncerrando...')
            sleep(1)
            interrompe = True
            print('Programa encerrado')
            break



"""(primeiro a cabeça, depois o tronco, de seguida pernas e braços e termina-se com olhos, nariz e boca)"""
