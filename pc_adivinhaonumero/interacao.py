from random import randint
from pc_adivinhaonumero.funcoes import *
from time import sleep


usu = int()
num = randint(-1000, 1000)
interrompe = False


linha()
print('O computador esconde um número, seu objetivo é adivinhá-lo!'.center(80))
linha()

print(f'{formatacao("sublinhado", "-1000 <= Valor <= 1000")}'.rjust(87))

while not interrompe:
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

    if usu == num:
        break

    if num >= 0:
        if num < usu <= num + 100:
            linha()
            print(f'>>{formatacao("vermelho", "Quente!!")} Você tentou o número {usu}. Tente um número menor')
            linha()
        elif num > usu >= num - 100:
            linha()
            print(f'>> Seu número foi {usu}. {formatacao("verde", "Talvez você queira tentar un número maior...")}')
            linha()
    elif num < 0:
        if num > usu >= num - 100:
            linha()
            print(f'>>{formatacao("vermelho", "Tá perto!!")} Seu número foi {usu}. Tente um número maior')
            linha()
        elif num < usu < num + 100:
            linha()
            print(f'>> Seu número foi {usu}. {formatacao("verde", "Talvez você queira tentar um número menor...")}')
            linha()

if usu == num:
    sleep(1)
    print(f'{formatacao("verde", "Parabéns!! Você acertou o número: ")} {num}.')
