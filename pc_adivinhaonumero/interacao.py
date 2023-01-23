from random import randint
from pc_adivinhaonumero.funcoes import *
from time import sleep


usu = int()
num = randint(-1000, 1000)
interrompe = False
print(num)

linha()
print('O computador esconde um número, seu objetivo é adivinhá-lo!'.center(80))
linha()

print(f'{formatacao("sublinhado", "-1000 <= Valor <= 1000")}'.rjust(87))

while usu != num or not interrompe:
    try:
        usu = int(input('Sua tentativa>> '))
    except (ValueError, TypeError):
        print(formatacao('vermelho', 'Erro!! Digite uma valor válido'))
    except KeyboardInterrupt:
        interrompe = True
        print('\nEncerrando...')
        sleep(1.5)
        print('O programa foi encerrado durante sua execução.')
        break

    if num >= 0:
        if num < usu <= num + 100:
            linha()
            print(f'>>{formatacao("vermelho", "Quente!!")} Tente um número menor')
            linha()
        elif num > usu >= num - 100:
            linha()
            print(f'>>{formatacao("verde", "Talvez você queira tentar un número maior...")}')
            linha()
    elif num < 0:
        if num > usu >= num - 100:
            linha()
            print(f'>>{formatacao("vermelho", "Tá perto!!")} Tente um número maior')
            linha()
        elif num < usu < num + 100:
            print(f'{formatacao("verde", "Talvez você queira tentar um número menor...")}')