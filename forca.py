"""Esse arquivo corresponde ao jogo de forca e toda sua lógica"""


def jogar():
    '''função que retorna o jogo por si só'''

    bem_vindo_msg = 'Bem vindo ao jogo da Forca!'
    enfeite = '*' * 80
    print(f'{enfeite}\n{bem_vindo_msg:^80}\n{enfeite}')


if (__name__ == '__main__'):
    jogar()
