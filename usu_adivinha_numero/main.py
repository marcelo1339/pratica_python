"""O usuário vai digitar um número e o PC vai tentar adivinhá-lo. Conforme o PC tenta adivinhar o usuário vai "comandar"
os palpites dele dizendo se ele deve chutar mais para baixo ou mais para cima."""
# Falta fazer o programa não gerar números repetidos

from random import randint
from time import sleep
from usu_adivinha_numero.funcoes import *

interrompe = False
n = opc = pc = 0
tentativas = set()

linha()
print('Digite um número entre -1000 e 1000, para que eu possa tentar adivinhá-lo'.center(80))

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

if pc not in tentativas:
    pc = randint(-1000, 1000)

while not interrompe:
    linha()
    print(f'Seu número foi {n}.')
    print(f'Minha tentativa {pc}.')
    if pc == n:
        print(f'{formatacao("verde", "Acertei!!")} Parece que estou com sorte.')
        break
    elif pc != n:
        tentativas = pc

        linha()
        print('Me guie!'.center(80))
        linha()

        print('''[1] Chute mais para cima
[2] Chute mais para baixo
[3] Fechar ''')

        while not interrompe:
            try:
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
        if opc == 1:
            pc = randint(pc, pc + 100)
            tentativas = pc
        elif opc == 2:
            pc = randint(pc - 100, pc)
            tentativas = pc
        elif opc == 3:
            interrompe = True
            print('Encerrando...')
            sleep(1)
            print('Volte sempre!!')

