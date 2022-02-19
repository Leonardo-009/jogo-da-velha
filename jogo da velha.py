import random
from turtle import goto

print("boa sorte!")

borda = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
vencedor = None
gameRunning = True


def placaDeImpressão(borda):
    print(borda[0] + " | " + borda[1] + " | " + borda[2])
    print("|---------|")
    print(borda[3] + " | " + borda[4] + " | " + borda[5])
    print("|---------|")
    print(borda[6] + " | " + borda[7] + " | " + borda[8])


def playerInput(borda):
    inp = int(input("Select a spot 1-9: "))
    if borda[inp-1] == "-":
        borda[inp-1] = currentPlayer
    else:
        print("OPA, o jogador já está nesse local! Seu NB. ")


def checkHorizontle(borda):
    global vencedor
    if borda[0] == borda[1] == borda[2] and borda[0] != "-":
        vencedor = borda[0]
        return True
    elif borda[3] == borda[4] == borda[5] and borda[3] != "-":
        vencedor = borda[3]
        return True
    elif borda[6] == borda[7] == borda[8] and borda[6] != "-":
        vencedor = borda[6]
        return True


def checkRow(borda):
    global vencedor
    if borda[0] == borda[3] == borda[6] and borda[0] != "-":
        vencedor = borda[0]
        return True
    elif borda[1] == borda[4] == borda[7] and borda[1] != "-":
        vencedor = borda[1]
        return True
    elif borda[2] == borda[5] == borda[8] and borda[2] != "-":
        vencedor = borda[3]
        return True


def checkDiag(borda):
    global vencedor
    if borda[0] == borda[4] == borda[8] and borda[0] != "-":
        vencedor = borda[0]
        return True
    elif borda[2] == borda[4] == borda[6] and borda[4] != "-":
        vencedor = borda[2]
        return True


def checkIfWin(borda):
    global gameRunning
    if checkHorizontle(borda):
        placaDeImpressão(borda)
        print(f"O vencedor é {vencedor}! Fez mais que sua Obrigação")
        gameRunning = False

    elif checkRow(borda):
        placaDeImpressão(borda)
        print(f"O vencedor é {vencedor}! Fez mais que sua Obrigação")
        gameRunning = False

    elif checkDiag(borda):
        placaDeImpressão(borda)
        print(f"O vencedor é {vencedor}! Fez mais que sua Obrigação")
        gameRunning = False


def checkIfTie(borda):
    global gameRunning
    if "-" not in borda:
        placaDeImpressão(borda)
        print("É uma gravata!")
        gameRunning = False


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(borda):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if borda[position] == "-":
            borda[position] = "O"
            switchPlayer()


while gameRunning:
    placaDeImpressão(borda)
    playerInput(borda)
    checkIfWin(borda)
    checkIfTie(borda)
    switchPlayer()
    computer(borda)
    checkIfWin(borda)
    checkIfTie(borda)
