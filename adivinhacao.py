"""Esse arquivo corresponde ao jogo de adivinhação e toda sua lógica"""
# importando bibliotecas
from random import randint
import time


def jogar():
    '''função que retorna o jogo por si só' '''

    # mensagem de boas vindas
    print_msg_boas_vindas()

    # explicando o jogo
    explica_jogo()

    # determinando variaveis do jogo
    numero_secreto = randint(1, 101)
    print(numero_secreto)
    tentativas_totais = 0
    pontos = 1000

    # adicionando grau de dificuldade
    tentativas_totais = escolhe_dificuldade(tentativas_totais)

    # loop
    verifica_chute(tentativas_totais, numero_secreto, pontos)

    print("teste 123")

    print_endgame_msg()


def explica_jogo():
    print('O jogo é simples!')
    print('Para ganhar você precisa acertar o número que tenho na memória.')
    print('DICA IMPORTANTE: Eu só penso em números de 1 a 100!')


def escolhe_dificuldade(tentativas_totais):
    print('Em qual nivel de dificuldade você quer jogar?')
    print('(1) Fácil - (2) Médio - (3) Difícil')
    nivel = int(input('Defina o nível: '))
    if (nivel == 1):
        tentativas_totais = 20
    elif (nivel == 2):
        tentativas_totais = 10
    else:
        tentativas_totais = 5
    return tentativas_totais


def print_msg_boas_vindas():
    bem_vindo_msg = 'Bem vindo ao jogo de Adivinhação!'
    enfeite = '*' * 80
    print(f'{enfeite}\n{bem_vindo_msg:^80}\n{enfeite}')


def verifica_chute(tentativas_totais, numero_secreto, pontos):
    """ função que verifica se o chute dado pelo usuário é igual
    ao número_secreto dentro de x rodadas
    """
    # for parâmetros - range(start, stop, [step])
    for rodada in range(1, tentativas_totais + 1):
        chute = int(input('Digite seu palpite de sorte: '))

        if (chute < 1 or chute > 100):
            print('O palpite deve estar entre 1 e 100! Tente novamente.')
            continue  # reinicia o laço

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print('Processando...')
        time.sleep(1)

        print(f'Tentativa {rodada} de {tentativas_totais}')
        if (acertou):
            print_msg_acertou(pontos)
            break  # interrompe o laço se acertou
        if (maior):
            if rodada == tentativas_totais:
                print_msg_perdedor(numero_secreto)
            else:
                print('Você errou! O seu chute foi maior do que o "\
                     "número secreto.')
        if (menor):
            if rodada == tentativas_totais:
                print_msg_perdedor(numero_secreto)
            else:
                print('Você errou! O seu chute foi menor do que o "\
                     "número secreto.')

        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos


def print_msg_acertou(pontos):
    print('O seu palpite está...')
    time.sleep(0.5)
    print('CORRETO!!! PARABÉNS')
    print(f'Você fez {pontos} pontos!')


def print_endgame_msg():
    endgame_msg = 'Fim do Jogo'
    enfeite = '*' * 80
    print(f'{enfeite}\n{endgame_msg:^80}\n{enfeite}')


def print_msg_perdedor(numero_secreto):
    print("Você perdeu!!!")
    print(f"O número que eu havia pensado era {numero_secreto}")


if (__name__ == '__main__'):
    jogar()
