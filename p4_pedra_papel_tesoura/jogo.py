"""Pedra, papel ou tesoura"""
from p4_pedra_papel_tesoura.funcoes import *
from time import sleep
from random import choice


def jokenpo():
    interrompe = False
    continua = ''
    while True:
        if interrompe:
            break
        if continua.upper() == 'N':
            sleep(1)
            linha()
            print(f'{formatacao("verde", "Volte sempre!!"):-^68}')
            break

        interrompe = False
        p_p_t = list()
        opc = int()
        pc = usu = str()


        linha()
        print(f'{"[1] Pedra [2] Papel [3] Tesoura":^60}')

        while not interrompe or continua.upper() == 'S':
            try:
                linha()
                opc = int(input('>> Sua escolha '))
                if 1 <= opc <= 3:
                    break
                print(formatacao('vermelho', 'ESCOLHA UMA OPÇÃO VÁLIDA'))
            except (ValueError, TypeError):
                print(formatacao('vermelho', 'ESCOLHA UMA OPÇÃO VÁLIDA'))
            except KeyboardInterrupt:
                interrompe = True
                print('\nEncerrando...')
                sleep(1)
                print('O programa foi encerrado!!')

        if not interrompe or continua.upper() == 'S':
            p_p_t = ['Pedra', 'Papel', 'Tesoura']
            usu = p_p_t[opc - 1]
            pc = choice(p_p_t)  # "Choice" vem de random

            # Empate
            if (pc == usu == 'Pedra') or (pc == usu == 'Papel') or (pc == usu == 'Tesoura'):
                linha()
                print(f'{formatacao("amarelo", "Empate!!")} Você escolheu {formatacao("sublinhado", f"{usu}")}.\n'
                      f'Eu escolhi {formatacao("sublinhado", f"{pc}")}.')
            # usuário ganha
            elif (usu == 'Pedra' and pc == 'Tesoura') or (usu == 'Papel' and pc == 'Pedra') or (usu == 'Tesoura' and pc == 'Papel'):
                linha()
                print(f'{formatacao("verde", "Você ganhou!!")} Sua escolha foi {formatacao("sublinhado", f"{usu}")}.\n'
                      f'Minha escolha foi {formatacao("sublinhado", f"{pc}")}.')
            # pc ganha
            elif (pc == 'Pedra' and usu == 'Tesoura') or (pc == 'Papel' and usu == 'Pedra') or (pc == 'Tesoura' and usu == 'Papel'):
                linha()
                print(f'{formatacao("vermelho", "Ganhei!!")} Sua escolha foi {formatacao("sublinhado", f"{usu}")}.\n'
                      f'Minha escolha foi {formatacao("sublinhado", f"{pc}")}.')

        while not interrompe or continua.upper() == 'S':
            try:
                linha()
                continua = str(input('Quer continuar?? [S/N] ')).strip().upper()[0]
                if continua in 'SN':
                    break
                print(f'{formatacao("vermelho", "Escolha uma opção válida!!")}')
            except (ValueError, TypeError, IndexError):
                print(f'{formatacao("vermelho", "Escolha uma opção válida")}')
            except KeyboardInterrupt:
                interrompe = True
                print('Encerrando...')
                sleep(1)
                print('O programa foi encerrado!!')


# Principal
print(jokenpo())
