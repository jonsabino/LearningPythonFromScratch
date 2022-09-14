# importando bibliotecas
from random import randint
import time

# mensagem de boas vindas
bem_vindo_msg = "Bem vindo ao jogo de Adivinhação!"
enfeite = "*" * 80
print(f"{enfeite}\n{bem_vindo_msg:^80}\n{enfeite}")

# explicando o jogo
print("O jogo é simples!")
print("Para ganhar você precisa acertar o número que tenho na memória.")
print("DICA IMPORTANTE: Eu só penso em números de 1 a 10!")

# determinando variaveis do jogo
numero_secreto = randint(1, 10)
tentativas_totais = 3
rodada = 1

# loop
while (rodada <= tentativas_totais):
    chute = int(input("Digite seu palpite de sorte: "))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Processando...")
    time.sleep(2)

    print(f"Tentativa {rodada} de {tentativas_totais}")
    if acertou:
        print("O seu palpite está...")
        time.sleep(0.5)
        print("CORRETO!!! PARABÉNS")
    elif menor:
        print("Você errou! O seu chute foi MENOR do que o número secreto.")
    else:
        print("Você errou! O seu chute foi MAIOR do que o número secreto.")
    rodada += 1

endgame_msg = "Fim do Jogo"
print(f"{enfeite}\n{endgame_msg:^80}\n{enfeite}")
