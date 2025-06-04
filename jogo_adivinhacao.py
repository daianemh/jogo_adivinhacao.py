import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("O número é maior.")
        elif palpite > numero_secreto:
            print("O número é menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinhacao()
