# importando bibliotecas
from random import randint
import time

# mensagem de boas vindas
BEM_VINDO_MSG = "Bem vindo ao jogo de Adivinhação!"
ENFEITE = "*" * 80
print(f"{ENFEITE}\n{BEM_VINDO_MSG:^80}\n{ENFEITE}")

# explicando o jogo
print("O jogo é simples!")
print("Para ganhar você precisa acertar o número que tenho na memória.")
print("DICA IMPORTANTE: Eu só penso em números de 1 a 100!")

# determinando variaveis do jogo
NUMERO_SECRETO = randint(1, 101)
TENTATIVAS_TOTAIS = 0

# adicionando grau de dificuldade
print("Em qual nivel de dificuldade você quer jogar?")
print("(1) Fácil - (2) Médio - (3) Difícil")
NIVEL = int(input("Defina o nível: "))
if NIVEL == 1:
    TENTATIVAS_TOTAIS = 20
elif NIVEL == 2:
    TENTATIVAS_TOTAIS = 10
else:
    TENTATIVAS_TOTAIS = 5

# loop
for RODADA in range(1, TENTATIVAS_TOTAIS + 1): # for parametros - range(start, stop, [step])
    chute = int(input("Digite seu palpite de sorte: "))

    if chute < 1 or chute > 100:
        print("O palpite deve estar entre 1 e 100! Tente novamente.")
        continue  # reinicia o laço

    acertou = chute == NUMERO_SECRETO
    maior = chute > NUMERO_SECRETO
    menor = chute < NUMERO_SECRETO

    print("Processando...")
    time.sleep(2)

    print(f"Tentativa {RODADA} de {TENTATIVAS_TOTAIS}")
    if acertou:
        print("O seu palpite está...")
        time.sleep(0.5)
        print("CORRETO!!! PARABÉNS")
        break  # interrompe o laço se acertou
    if menor:
        print("Você errou! O seu chute foi MENOR do que o número secreto.")
    else:
        print("Você errou! O seu chute foi MAIOR do que o número secreto.")
    RODADA += 1

ENDGAME_MSG = "Fim do Jogo"
print(f"{ENFEITE}\n{ENDGAME_MSG:^80}\n{ENFEITE}")
