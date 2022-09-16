"""Esse arquivo corresponde ao jogo de adivinhação e toda sua lógica"""
# importando bibliotecas
from random import randint
import time


def jogar():
    '''função que retorna o jogo por si só' '''
    # mensagem de boas vindas
    bem_vindo_msg = 'Bem vindo ao jogo de Adivinhação!'
    enfeite = '*' * 80
    print(f'{enfeite}\n{bem_vindo_msg:^80}\n{enfeite}')

    # explicando o jogo
    print('O jogo é simples!')
    print('Para ganhar você precisa acertar o número que tenho na memória.')
    print('DICA IMPORTANTE: Eu só penso em números de 1 a 100!')

    # determinando variaveis do jogo
    numero_secreto = randint(1, 101)
    tentativas_totais = 0
    pontos = 1000

    # adicionando grau de dificuldade
    print('Em qual nivel de dificuldade você quer jogar?')
    print('(1) Fácil - (2) Médio - (3) Difícil')
    nivel = int(input('Defina o nível: '))
    if (nivel == 1):
        tentativas_totais = 20
    elif (nivel == 2):
        tentativas_totais = 10
    else:
        tentativas_totais = 5

    # loop
    # for parametros - range(start, stop, [step])
    for rodada in range(1, tentativas_totais + 1):
        chute = int(input('Digite seu palpite de sorte: '))

        if (chute < 1 or chute > 100):
            print('O palpite deve estar entre 1 e 100! Tente novamente.')
            continue  # reinicia o laço

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        maior = chute < numero_secreto

        print('Processando...')
        time.sleep(2)

        print(f'Tentativa {rodada} de {tentativas_totais}')
        if (acertou):
            print('O seu palpite está...')
            time.sleep(0.5)
            print('CORRETO!!! PARABÉNS')
            print(f'Você fez {pontos} pontos!')
            break  # interrompe o laço se acertou
        if (maior):
            print('Você errou! O seu chute foi maior do que o número secreto.')
        else:
            print('Você errou! O seu chute foi maior do que o número secreto.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

    endgame_msg = 'Fim do Jogo'
    print(f'{enfeite}\n{endgame_msg:^80}\n{enfeite}')


if (__name__ == '__main__'):
    jogar()
