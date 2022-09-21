"""Esse arquivo corresponde ao jogo de forca e toda sua lógica"""
import random


def jogar():
    '''função que retorna o jogo por si só'''
    # funcoes
    print_bem_vindo()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            print(f"Ops, você errou! Faltam {(7 - erros)} tentativas.")

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print_msg_vencedor()
    else:
        print_msg_perdedor(palavra_secreta)


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


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ").strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[i] = letra
        i += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("     _______________ ")
    print("    /               \ ")
    print("   /                 \ ")
    print("/\/                   \/\ ")
    print("\ |   XXXX     XXXX   | / ")
    print(" \|   XXXX     XXXX   |/ ")
    print("  |   XXX       XXX   | ")
    print("  |                   | ")
    print("  \__      XXX      __/ ")
    print("    |\     XXX     /| ")
    print("    | |           | | ")
    print("    | I I I I I I I | ")
    print("    |  I I I I I I  | ")
    print("    \_             _/ ")
    print("      \_         _/ ")
    print("        \_______/ ")


if (__name__ == '__main__'):
    jogar()
