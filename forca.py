"""Esse arquivo corresponde ao jogo de forca e toda sua lógica"""

import random


def jogar():
    '''função que retorna o jogo por si só'''

    # funcoes
    print_bem_vindo()
    palavra_secreta = carrega_palavra_secreta()

    # List Comprehension
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ").strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {(6 - erros)} tentativas.")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print("Parabéns!!! Você ganhou.")
    else:
        print("Você perdeu!"
              f"A palavra era {palavra_secreta}. Mais sorte na próxima.")

    print("Fim do Jogo")


def print_bem_vindo():
    """imprime a mensagem de boas vindas ao usuário"""
    bem_vindo_msg = 'Bem vindo ao jogo da Forca!'
    enfeite = '*' * 80
    print(f'{enfeite}\n{bem_vindo_msg:^80}\n{enfeite}')


def carrega_palavra_secreta():
    """Abre o arquivo onde estão as palavras jogaveis,
    gera um número aleatório que será resposnável por escolher
    a palavra a ser jogada e a retorna
    """
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()
    return palavra_secreta


if (__name__ == '__main__'):
    jogar()
