print("********************************")
print("Bem vindo ao jogo de advinhação!")
print("********************************")

numeroSecreto = 42
tentativasTotais = 3
rodada = 1
while(rodada <= tentativasTotais):
    print("Tentantiva: ", rodada, "de ", tentativasTotais)
    chute = int(input("Digite o seu número: "))

    acerto = chute == numeroSecreto
    maior  = chute > numeroSecreto
    menor  = chute < numeroSecreto


    rodada = rodada + 1
    if (acerto):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")