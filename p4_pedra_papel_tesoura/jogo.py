"""Pedra, papel ou tesoura"""
from p4_pedra_papel_tesoura.funcoes import *
from time import sleep
from random import choice


def jokenpo():
    interrompe = False
    p_p_t = list()
    opc = int()
    pc = usu = str()


    linha()
    print(f'{"[1] Pedra [2] Papel [3] Tesoura":^60}')

    while not interrompe:
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


    p_p_t = ['Pedra', 'Papel', 'Tesoura']
    usu = p_p_t[opc - 1]
    pc = choice(p_p_t)

    # Empate
    if (pc == usu == 'Pedra') or (pc == usu == 'Papel') or (pc == usu == 'Tesoura'):
        linha()
        print(f'{formatacao("amarelo", "Empate!!")} Você escolheu {formatacao("sublinhado", f"{usu}")}.'
              f' Eu escolhi {formatacao("sublinhado", f"{pc}")}')



print(jokenpo())
