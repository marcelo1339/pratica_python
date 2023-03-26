"""Todas as palavras que estão no arquivo -palavras.txt- foram retiradas do perfil Python Pro:
https://github.com/pythonprobr/palavras"""

from p5_jogo_da_forca.funcoes import *
from time import sleep


interrompe = acertou = False
usu = str()
palavra = list()
letra_nao_existe = list()
word = list()
indice_letra_repetida = list()
errou = repetidas = total_tentativas = dificuldade = 0

while True:
    try:
        linha()
        print('Em qual dificuldade deseja jogar??'.center(60))
        print('[1] Fácil [2] Médio [3] Difícil'.center(60))
        linha()

        dificuldade = int(input('Sua escolha>> '))

        if 1 <= dificuldade <= 3:
            break
        print('Escolha uma das opções!')

    except (TypeError, ValueError, IndexError):
        print('Escolha uma das opções!')
    except KeyboardInterrupt:
        print('\nEncerrando...')
        sleep(1)
        break

if dificuldade == 1:
    total_tentativas = 20
elif dificuldade == 2:
    total_tentativas = 15
elif dificuldade == 3:
    total_tentativas = 10


for l in palavra_txt('palavras.txt'):
    word.append(l.lower())

del word[-1]

for l in word:
    palavra.append('_')


while True:
    if errou == total_tentativas or interrompe or acertou:
        break

    while True:
        try:
            linha()
            print('Jogo da forca'.center(60))
            linha()
            print(word)
            print(f'--Você tem {total_tentativas - errou} tentativas.')
            print(f'--A palavra tem {len(word)} letras.')
            print('--Tenha em mente que a palavra pode conter letras com acentos \n como "í, é, â, õ" entre outras.')

            linha()
            usu = str(input('>>Tente uma letra: ')).strip().lower()[0]

            if not usu.isalpha():
                print('Por favor, tente uma letra!')

            if usu not in word and usu.isalpha():
                if usu not in letra_nao_existe:
                    letra_nao_existe.append(usu)
                errou += 1

            if errou == total_tentativas:
                print(':-( Parece que você perdeu!')
                break

            print(f'Não estão na palavra: {letra_nao_existe}')

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
                elif repetidas == 1:
                    for letra in word:
                        posicao = word.index(usu)
                        for elemento in palavra:
                            if usu == letra:
                                palavra.pop(posicao)
                                palavra.insert(posicao, usu)

            print('Sua palavra: ', end='')
            for elemento in palavra:
                print(elemento, end='')
            print()

            if '_' not in palavra:
                acertou = True
                break

        except (ValueError, TypeError, IndexError) as erro:
            print('Por favor, tente uma letra!')
            print(f'Seu erro foi {erro}')
        except KeyboardInterrupt:
            print('\nEncerrando...')
            sleep(1)
            interrompe = True
            print('Programa encerrado')
            break

if acertou:
    linha()
    print('Meus parabéns!! Você acertou a palavra!!')

if errou == 9:
    linha()
    print(f'A palavra era: ', end='')
    for letra in word:
        print(letra, end='')
    print()
