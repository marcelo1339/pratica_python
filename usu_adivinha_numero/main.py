"""O usuário vai digitar um número e o PC vai tentar adivinhá-lo. Conforme o PC tenta adivinhar o usuário vai "comandar"
os palpites dele dizendo se ele deve chutar mais para baixo ou mais para cima."""

from random import randint
from time import sleep
from usu_adivinha_numero.funcoes import *

interrompe = False
n = 0
tentativas = set()

print('Digite um número entre -1000 e 1000, para que eu possa tentar adivinhá-lo')

while not interrompe:
    try:
        linha()
        n = int(input('>> '))
        if -1000 <= n <= 1000:
            break
        print('Números entre -1000 e 1000...')
    except (ValueError, TypeError):
        print(f'>> {formatacao("vermelho", "Erro!!")} Digite apenas números inteiros.')
    except KeyboardInterrupt:
        interrompe = True
        print('\nEncerrando...')
        sleep(1)
        print('O Programa foi encerrado antes do fim.')

pc = randint(-1000, 1000)

while not interrompe:
    print(f'Minha tentativa {pc}.')
    if pc == n:
        print(f'{formatacao("verde", "Acertei!!")} Parece que estou com sorte.')
    elif pc != n:
        tentativas = pc
        print(tentativas)
        linha()
        print('Me guie!'.center(60))
        linha()

        print('''[1] Chute mais para cima
[2] Chute mais para baixo
[3] Fechar ''')
        try:
            while True:
                opc = int(input('\n>>Sua escolha '))
                if 1 <= opc <= 3:
                    break
                print('Escolha uma das opções!')
        except (ValueError, TypeError):
            linha()
            print('Apenas números inteiros')
        except KeyboardInterrupt:
            interrompe = True
            print('\nEncerrando...')
            sleep(1)
            print('O programa foi encerrado antes do fim.')






