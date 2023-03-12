from random import randint

print("********************************")
print("Bem vindo ao jogo de advinhação!")
print("********************************")

numeroSecreto = randint(1,100)

tentativasTotais = 0
pontos = 1000
rodada = 1

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Define o nível: "))

if (nivel == 1):
    tentativasTotais = 20
elif (nivel == 2):
    tentativasTotais = 10
else:
    tentativasTotais = 5
while(rodada <= tentativasTotais):
    print("Tentantiva: ", rodada, "de ", tentativasTotais)
    chute = int(input("Digite o seu número: "))
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    acerto = chute == numeroSecreto
    maior  = chute > numeroSecreto
    menor  = chute < numeroSecreto


    rodada = rodada + 1
    if (acerto):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        pontosPerdidos = abs(numeroSecreto - chute)
        pontos = pontos -pontosPerdidos
