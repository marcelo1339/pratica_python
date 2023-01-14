from random import randint
from funcoes import *

# Variáveis
elementos_historia = dict()

frases = list()
substantivos = list()
objetos = list()
verbos = list()
lugares = list()
nomes = list()
selecionados = list()

qtd_nom = qtd_lugar = qtd_verbo = qtd_obj = qtd_subs = qtd_fra = ale = 0
nom = lug = ver = obj = subs = fra = ''
continua = 'S'
interrompe = False

# Recebendo dados do usuário
while True:
    try:
        linha()
        nom = str(input('Nome qualquer (pode ser de um personagem fictício): ')).strip().title()
    except (ValueError, TypeError):
        print('Digite um valor válido!')
    except KeyboardInterrupt:
        interrompe = True
        encerramento()
        break
    if nom in nomes:
        print(cores('vermelho', 'Esse ja foi.'))
    elif len(nom) == 0:
        print(cores('vermelho', 'Vazio não pode!!'))
    elif nom not in nomes or len(nom) != 0:
        nomes.append(nom)
        qtd_nom += 1
        print(cores('verde', 'Nome adicionado com sucesso!!'))

    if qtd_nom >= 4 and not interrompe:
        while True:
            try:
                linha()
                continua = str(input('Quer adicionar mais algum nome? [S/N] ')).strip().upper()[0]
                if continua in 'SN':
                    break
                print(cores('vermelho', 'Erro!!'), 'Escolha uma opção válida!')
            except (ValueError, TypeError, IndexError):
                print(cores('vermelho', 'Erro!!'), 'Escolha uma opção válida!')
            except KeyboardInterrupt:
                interrompe = True
                encerramento()
                break

    if continua == 'N' and interrompe is False:
        continua = 'S'
        while continua == 'S' and interrompe is False:
            try:
                linha()
                lug = str(input('Nome de um lugar qualquer: ')).strip()
            except (TypeError, ValueError):
                print('Digite um valor válido!')
            except KeyboardInterrupt:
                interrompe = True
                encerramento()
                break
            if lug in lugares:
                print(cores('vermelho', 'Esse ja foi!!'))
            elif len(lug) == 0:
                print(cores('vermelho', 'Vazio não pode!!'))
            elif lug not in lugares or len(lug) != 0:
                lugares.append(lug)
                print(cores('verde', 'Lugar adicionado com sucesso!!'))
                qtd_lugar += 1

            if qtd_lugar >= 3 and not interrompe:
                continua.replace('S', ' ')
                while True:
                    try:
                        linha()
                        continua = str(input('Deseja adicionar mais algum lugar??[S/N] ')).strip().upper()[0]
                        if continua in 'SN':
                            break
                        print(cores('vermelho', 'Escolha uma opção válida!!'))
                    except (ValueError, TypeError, IndexError):
                        print(cores('vermelho', 'Escolha uma opção válida!!'))
                    except KeyboardInterrupt:
                        interrompe = True
                        encerramento()
                        break

    if continua == 'N' and not interrompe:
        continua = 'S'
        while continua == 'S' and interrompe is False:
            try:
                linha()
                print('Serão 8 verbos, tente digitar verbos conjugados de diversas maneiras')
                ver = str(input('Digite um verbo: ')).strip()
            except (ValueError, TypeError):
                print(cores('vermelho', 'Digite um valor válido!!'))
            except KeyboardInterrupt:
                interrompe = True
                encerramento()
                break
            if ver in verbos:
                print(cores('vermelho', 'Esse já foi!!'))
            elif len(ver) == 0:
                print(cores('vermelho', 'Vazio não pode!!'))
            elif ver not in verbos or len(ver) != 0:
                verbos.append(ver)
                qtd_verbo += 1
                print(cores('verde', 'Verbo adicionado!!'))

            if qtd_verbo >= 8 and not interrompe:
                continua.replace('S', ' ')
                while True:
                    try:
                        linha()
                        continua = str(input('Quer adicionar outro verbo?[S/N] ')).strip().upper()[0]
                        if continua in 'SN':
                            break
                        print(cores('vermelho', 'Escolha uma opção válida!!'))
                    except (TypeError, ValueError, IndexError):
                        print(cores('vermelho', 'Escolha uma opção válida!!'))
                    except KeyboardInterrupt:
                        interrompe = True
                        encerramento()
                        break

    if continua == 'N' and not interrompe:
        continua = 'S'
        while continua == 'S' and interrompe is False:
            try:
                linha()
                obj = str(input('Digite o nome de um objeto: ')).strip()
            except (ValueError, TypeError):
                print(cores('vermelho', 'Escolha uma opção válida!!'))
            except KeyboardInterrupt:
                interrompe = True
                encerramento()
                break
            if obj in objetos:
                print(cores('vermelho', 'Esse já foi!!'))

            if len(obj) == 0:
                print(cores('vermelho', 'Vazio não pode'))

            if obj not in objetos and len(obj) != 0:
                objetos.append(obj)
                qtd_obj += 1
                print(cores('verde', 'Objeto adicionado com sucesso!!'))

            if qtd_obj >= 3 and not interrompe:
                continua.replace('S', ' ')
                while True:
                    try:
                        linha()
                        continua = str(input('Quer adicionar outro objeto? [S/N] ')).strip().upper()[0]
                        if continua in 'SN':
                            break
                        print(cores('vermelho', 'Escolha uma opção válida!!'))
                    except (TypeError, ValueError, IndexError):
                        print(cores('vermelho', 'Escolha uma opção válida!!'))
                    except KeyboardInterrupt:
                        interrompe = True
                        encerramento()
                        break

    if continua == 'N' and not interrompe:
        continua = 'S'
        while continua == 'S' and interrompe is False:
            try:
                linha()
                subs = str(input('Digite um substantivo qualquer: ')).strip()
            except (ValueError, TypeError):
                print(cores('vermelho', 'Digite um valor válido!!'))
            except KeyboardInterrupt:
                interrompe = True
                encerramento()
                break
            if subs in substantivos:
                print(cores('vermelho', 'Repetido não pode!!'))

            if len(subs) == 0:
                print(cores('vermelho', 'Vazio não pode!!'))

            if subs not in substantivos and len(subs) != 0:
                substantivos.append(subs)
                qtd_subs += 1
                print(cores('verde', 'Substantivo adicionado com sucesso!!'))

            if qtd_subs >= 1 and not interrompe:
                continua.replace('S', ' ')
                while True:
                    try:
                        linha()
                        continua = str(input('Quer adicionar outro substantivo [S/N]''?? ')).strip().upper()[0]
                        if continua in 'SN':
                            break
                        print(cores('vermelho', 'Escolha uma opção válida!!'))
                    except (ValueError, IndexError, TypeError):
                        print(cores('vermelho', 'Escolha uma opção válida!!'))
                    except KeyboardInterrupt:
                        interrompe = True
                        encerramento()
                        break

    if continua == 'N' and not interrompe:
        continua = 'S'
        while continua == 'S' and interrompe is False:
            try:
                linha()
                fra = str(input('Digite uma frase de efeito: ')).strip().capitalize()
            except (ValueError, TypeError):
                print(cores('vermelho', 'Digite um valor válido!!'))
            except KeyboardInterrupt:
                interrompe = True
                encerramento()
                break
            if fra in frases:
                print(cores('vermelho', 'Repetido não pode!!'))

            if len(fra) == 0:
                print(cores('vermelho', 'Vazio não pode'))

            if fra not in frases and len(fra) != 0:
                frases.append(fra)
                qtd_fra += 1
                print(cores('verde', 'Frase adicionada com sucesso!!'))

            if qtd_fra >= 1 and not interrompe:
                continua.replace('S', ' ')
                while True:
                    try:
                        linha()
                        continua = str(input('Quer adicionar outra frase?? [S/N] ')).strip().upper()[0]
                        if continua in 'SN':
                            break
                        print(cores('vermelho', 'Erro'), 'Escolha uma opção válida!!')
                    except (IndexError, TypeError, ValueError):
                        print(cores('vermelho', 'Erro!!'), 'Digite uma opção válida!!')
                    except KeyboardInterrupt:
                        interrompe = True
                        encerramento()
                        break
    if continua == 'N':
        sleep(1)
        break

    if interrompe:
        break

linha()
if len(substantivos) == 0 and len(objetos) == 0 and len(verbos) == 0 and len(lugares) == 0 and len(nomes) == 0 and len(
        frases) == 0:
    print(cores('amarelo', 'Nenhum dado foi adicionado.'))
else:
    print(cores('verde', 'Os dados foram adicionados!!'))


ale = randint(0, len(nomes) - 1)
elementos_historia['mãe'] = nomes[ale]
del nomes[ale]

ale = randint(0, len(nomes) - 1)
elementos_historia['pai'] = nomes[ale]
del nomes[ale]

ale = randint(0, len(nomes) - 1)
elementos_historia['principal'] = nomes[ale]
del nomes[ale]

ale = randint(0, len(nomes) - 1)
elementos_historia['amigo'] = nomes[ale]
del nomes[ale]

for c in range(0, 3):
    ale = randint(0, len(lugares) - 1)
    elementos_historia[f'lugar{c}'] = lugares[ale]
    del lugares[ale]

for c in range(0, 8):
    ale = randint(0, len(verbos) - 1)
    elementos_historia[f'verbo{c}'] = verbos[ale]
    del verbos[ale]

for c in range(0, 3):
    ale = randint(0, len(objetos) - 1)
    elementos_historia[f'objeto{c}'] = objetos[ale]
    del objetos[ale]

ale = randint(0, len(substantivos) - 1)
elementos_historia['substantivo'] = substantivos[ale]
del substantivos[ale]

ale = randint(0, len(frases) - 1)
elementos_historia['frasefeito'] = frases[ale]
del frases[ale]


print('-=' * 50)
print(f'{"Aprecie sua obra...":^100}')
print('-=' * 50)
sleep(1)

print(f"""
    O jovem {elementos_historia['principal']} estava em seu {elementos_historia['lugar0']} enquanto seus país 
conversavam em voz baixa, em outro cômodo... Ele estava em chamada com {elementos_historia['amigo']}, seu amigo, 
justamente falando sobre desconfiar do comportamento de seus pais.

{elementos_historia['principal']} diz:
    -Cara, eu tô te falando, eles tem {elementos_historia['verbo0']} há pelo menos um mês.
{elementos_historia['amigo']} responde:
    -Isso não me surpreende muito, já que quando meus pais se separaram, eles já estavam
{elementos_historia['verbo1']} há um certo tempo...
{elementos_historia['principal']}:
    -É, eu sei que essas coisas acontecem, mas eles poderiam pelo menos tentar disfarçar, já tá meio ridículo ver
eles {elementos_historia['verbo2']} o tempo todo.

    -{elementos_historia['principal']} toma um susto e derruba o celular pois escuta a voz de seus pais logo atrás da 
{elementos_historia['objeto0']}, e, antes que pudesse encerrar a chamada com {elementos_historia['amigo']} eles entram 
no {elementos_historia['lugar0']}-

Sua mãe, {elementos_historia['mãe']} diz:
    -Oi {elementos_historia['principal']}, tá fazendo o que?
{elementos_historia['principal']} -Nada demais mãe, eu tava só {elementos_historia['verbo3']} um pouco.
Seu pai, {elementos_historia['pai']} diz:
    -Eu escutei o barulho de alguma coisa caindo. Você quebrou o quê?
{elementos_historia['principal']} -Ah! O controle do meu {elementos_historia['objeto1']} caiu no chão.
{elementos_historia['pai']} -Certo, eu e sua mãe queremos trocar uma palavrinha com você...

    -{elementos_historia['pai']} levanta as sobrancelhas e olha para {elementos_historia['mãe']}-

{elementos_historia['mãe']} -{elementos_historia['principal']}, você sabe que seus pais se amam muito né?

    -{elementos_historia['principal']} acena "sim" com a cabeça-

-E quando duas pessoas se amam, elas não precisam estar necessáriamente {elementos_historia['verbo4']} o tempo 
inteiro...

    -{elementos_historia['pai']} interrompe-

-Pra ser sincero filho, a questão é que não tem jeito fácil de dizer isso... Sua mãe e eu estamos nos
{elementos_historia['verbo5']}.

    -{elementos_historia['principal']} não expressa muita reação fica apenas olhando e ouvindo os pais falarem-
    
-E você pode não gostar, mas isso faz parte da vida das
pessoas.
{elementos_historia['mãe']} -Eu vou morar em {elementos_historia['lugar1']} com uma amiga agora, e você sempre 
vai poder ir lá me ver.

    -O {elementos_historia['lugar0']} fica em silêncio por alguns segundos-

{elementos_historia['pai']} -A gente te ama filho. Eu acho que é melhor deixarmos você absorver isso por 
enquanto, qualquer coisa vamos estar na {elementos_historia['lugar2']}.

    -Os dois então saem-

    -{elementos_historia['principal']} senta na {elementos_historia['objeto2']} e fica olhando para o teto-

{elementos_historia['amigo']}, que escutou toda a conversa, diz:
    -Alô!! {elementos_historia['principal']}, você tá ai ainda?

    -{elementos_historia['principal']} se assusta, pois esqueceu que seu amigo ainda estava ali, e então pega o 
celular-

{elementos_historia['amigo']} -Cara... mesmo já passando por isso ainda é esquisito de presenciar...
{elementos_historia['principal']} -Pois é... é como se não tivesse uma maneira certa de lidar com 
{elementos_historia['substantivo']}.
{elementos_historia['amigo']} -Você vai ficar bem?
{elementos_historia['principal']} -Acho que vou ter que {elementos_historia['verbo6']}
-É como as pessoas sempre dizem "{elementos_historia['frasefeito']}".
-Vamos {elementos_historia['verbo7']} pra eu me distrair um pouco."""
      )
