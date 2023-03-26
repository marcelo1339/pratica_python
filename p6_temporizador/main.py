from time import sleep


def timer(horas, minutos, segundos):


    if minutos >= 60:
        horas += divmod(minutos, 60)[0]
        minutos = divmod(minutos, 60)[1]


    if segundos >= 60:
        minutos += divmod(segundos, 60)[0]
        segundos = divmod(segundos, 60)[1]

    print('Temporizador')

    while True:
        print(end='\r' f'{horas:0>2}:{minutos:0>2}:{segundos:0>2}')

        if segundos == 0 and minutos == 0 and horas == 0:
            break

        if minutos == 0 and segundos == 0:
            horas -= 1
            minutos += 60

        if segundos == 0:
            minutos -= 1
            segundos += 60


        segundos -= 1
        sleep(1)

    print('Acabou!!')


if __name__ == "__main__":
    timer(15, 0, 3)
