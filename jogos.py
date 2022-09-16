"""Aquivo que permite o usuário escolher qual dos jogos
das bibliotecas disponíveis ele irá jogar
"""
# importando jogos
import forca
import adivinhacao


def seleciona_jogo():
    '''função em que o usuário seleciona o jogo que irá rodar'''

    bem_vindo_msg = 'ESCOLHA O SEU JOGO!'
    enfeite = '*' * 80
    print(f'{enfeite}\n{bem_vindo_msg:^80}\n{enfeite}')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual sua escolha? '))

    if (jogo == 1):
        print('Jogando Forca')
        # chamando a função jogar da biblioteca forca
        forca.jogar()
    else:
        print('Jogando Adivinhação')
        # chamando a função jogar da biblioteca adivinhacao
        adivinhacao.jogar()


if (__name__ == '__main__'):
    seleciona_jogo()
