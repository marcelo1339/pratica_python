from random import randint
from funcoes import *

# Variáveis
verbos = list()
lugares = list()
nomes = list()
elementos_historia = dict()
qtd_nom = qtd_lugar = qtd_verbo = 0
nom = continua = lug = ''
interrompe = False

# Recebendo dados do usuário
while True:
    try:
        linha()
        nom = str(input('Nome qualquer (pode ser de um personagem fictício): ')).strip().capitalize()
    except (ValueError, TypeError):
        print('Digite um valor válido!')
    except KeyboardInterrupt:
        encerramento()
        break
    else:
        if nom in nomes:
            print(cores('vermelho', 'Esse ja foi.'))
        elif len(nom) == 0:
            print(cores('vermelho', 'Vazio não pode!!'))
        elif nom not in nomes or len(nom) != 0:
            nomes.append(nom)
            qtd_nom += 1
            print(cores('verde', 'Nome adicionado com sucesso!!'))

        if qtd_nom >= 4:
            while True:
                try:
                    linha()
                    continua = str(input('Quer adicionar mais algum nome? [S/N] ')).strip().upper()[0]
                    if continua in 'SN':
                        break
                    elif continua not in 'SN':
                        print(cores('vermelho', 'Erro!!'), 'Escolha uma opção válida!')
                except (ValueError, TypeError, IndexError):
                    print(cores('vermelho', 'Erro!!'), 'Escolha uma opção válida!')
                except KeyboardInterrupt:
                    interrompe = True
                    encerramento()
                    break
            if continua == 'N':
                while True:
                    try:
                        linha()
                        lug = str(input('Nome de um lugar qualquer: ')).strip()
                    except (TypeError, ValueError):
                        print('Digite um valor válido!')
                    except KeyboardInterrupt:
                        interrompe = True
                        encerramento()
                        break
                    else:
                        if lug in lugares:
                            print(cores('vermelho', 'Esse ja foi!!'))
                        elif len(lug) == 0:
                            print(cores('vermelho', 'Vazio não pode!!'))
                        elif lug not in lugares or len(lug) != 0:
                            lugares.append(lug)
                            print(cores('verde', 'Lugar adicionado com sucesso!!'))
                            qtd_lugar += 1
                        if qtd_lugar >= 4:
                            while True:
                                try:
                                    linha()
                                    continua = str(input('Deseja adicionar mais algum lugar??[S/N] ')).strip().upper()[0]
                                except (ValueError, TypeError, IndexError):
                                    print(cores('vermelho', 'Escolha uma opção válida!!'))
                                except KeyboardInterrupt:
                                    interrompe = True
                                    encerramento()
                                    break
                                else:
                                    if continua in 'SN':
                                        break
                                    print(cores('vermelho', 'Escolha uma opção válida!!'))
                            if continua == 'N':
                                while True:
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
                                    else:
                                        if ver in verbos:
                                            print(cores('vermelho', 'Esse já foi!!'))
                                        elif len(ver) == 0:
                                            print(cores('vermelho', 'Vazio não pode!!'))
                                        elif ver not in verbos or len(ver) != 0:
                                            verbos.append(ver)
                                            qtd_verbo += 1
                                            print(cores('verde', 'Verbo adicionado!!'))

                                        if qtd_verbo >= 8:
                                            while True:
                                                try:
                                                    linha()
                                                    continua = str(input('Quer adicionar outro verbo?[S/N] ')).strip().upper()[0]
                                                except (TypeError, ValueError, IndexError):
                                                    print(cores('vermelho', 'Escolha uma opção válida!!'))
                                                except KeyboardInterrupt:
                                                    interrompe = True
                                                    encerramento()
                                                    break
                                                else:
                                                    if continua in 'SN':
                                                        break
                                                    print(cores('vermelho', 'Escolha uma opção válida!!'))
    if interrompe:
        break


"""
    O jovem (protagonista) estava em seu (lugar) enquanto seus país conversavam em voz baixa, em outro cômodo...
    Ele estava em chamada com (amigo), seu amigo, justamente falando sobre desconfiar do comportamento de seus
    pais.

    (protagonista) diz:
        -Cara, eu tô te falando, eles tem (verbo-particípio) há pelo menos um mês.
    (amigo) responde:
        -Isso não me surpreende muito, já que quando meus pais se separaram, eles já estavam
        (verbo-passado) há um certo tempo...
    (protagonista):
        -É, eu sei que essas coisas acontecem, mas eles poderiam pelo menos tentar disfarçar, já tá meio ridículo ver
        eles (verbo-gerúndio) o tempo todo.

    -(protagonista) toma um susto e derruba o celular pois escuta a voz de seus pais logo atrás da (objeto), e, antes
    que pudesse encerrar a chamada com (amigo) eles entram no (lugar)-

    Sua mãe, (mãe) diz:
        -Oi (protagonista), tá fazendo o que?
        (protagonista) -Nada demais mãe, eu tava só (verbo-gerúndio) um pouco.
    Seu pai, (pai) diz:
        -Eu escutei o barulho de alguma coisa caindo. Você quebrou o quê?
        (protagonista) -Ah! O controle do meu (objeto) caiu no chão.
        (pai) -Certo, eu e sua mãe queremos trocar uma palavrinha com você...
        -(pai) levanta as sobrancelhas e olha para (mãe)-
        (mãe) -(protagonista), você sabe que seus pais se amam muito né?
        -(protagonista) acena "sim" com a cabeça-
        -E quando duas pessoas se amam, elas não precisam estar necessáriamente (substantivo) o tempo inteiro...
        -(pai) interrompe-
        -Pra ser sincero filho, a questão é que não tem jeito fácil de dizer isso... Sua mãe e eu estamos nos
        (verbo-gerúndio).
        -(protagonista) não expressa muita reação fica apenas olhando e ouvindo os pais falarem-
        -E você pode não gostar disso, mas se (verbo-infinitivo) faz parte da vida das
        pessoas.
        (mãe) -Eu vou morar em (lugar qualquer) com uma amiga agora, e você sempre vai poder ir lá me ver.
        -O (lugar) fica em silêncio por alguns segundos-
        (pai) -A gente te ama filho, mas eu acho que é melhor deixarmos você absorver isso por enquanto, qualquer coisa
        vamos estar na (lugar qualquer).
        -Os dois então saem-
        -(protagonista) senta na (objeto) e fica olhando para o teto-
    (amigo), que escutou toda a conversa, diz:
        -Alô!! (protagonista), você tá ai ainda?
        -(protagonista) se assusta, pois esqueceu que seu amigo ainda estava ali, e então pega o celular-
        (amigo) -Cara... mesmo já passando por isso ainda é esquisito de presenciar...
        (protagonista) -Pois é... é como se não tivesse uma maneira certa de lidar com (substantivo-plural).
        (amigo) -Você vai ficar bem?
        (protagonista) -Acho que vou ter que (verbo-infinitivo)
        -É como as pessoas sempre dizem "(frase de efeito)".
        - Vamos (verbo) pra eu me distrair um pouco"""
