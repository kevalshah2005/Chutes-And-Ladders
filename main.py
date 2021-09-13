import random
from termcolor import cprint

player1Square = 0
player2Square = 0
turnNumber = 1

chutes = {
  16 : 6,
  47 : 26,
  49 : 11,
  56 : 53,
  62 : 19,
  64 : 60,
  87 : 24,
  93 : 73,
  95 : 75,
  98 : 78
}

ladders = {
  1 : 38,
  4 : 14,
  9 : 31,
  21 : 42,
  28 : 84,
  36 : 44,
  51 : 67,
  71 : 91,
  80 : 100
}

def rollDie():
  discard = random.randint(1,6)
  return random.randint(1,6)

while (player1Square != 100) & (player2Square != 100):
  print("Turn " + str(turnNumber))
  player1roll = rollDie()
  player2roll = rollDie()

  player1NewSquare = player1Square + player1roll
  player2NewSquare = player2Square + player2roll

  if player1NewSquare in chutes:
    player1NewSquare = chutes[player1NewSquare]
  if player1NewSquare in ladders:
    player1NewSquare = ladders[player1NewSquare]
  
  if player2NewSquare in chutes:
    player2NewSquare = chutes[player2NewSquare]
  if player2NewSquare in ladders:
    player2NewSquare = ladders[player2NewSquare]

  if player1NewSquare > 100:
    player1NewSquare = player1Square
  if player2NewSquare > 100:
    player2NewSquare = player2Square

  print("Player 1 rolled a " + str(player1roll) + " and moved from space " + str(player1Square) + " to square " + str(player1NewSquare))
  print("Player 2 rolled a " + str(player2roll) + " and moved from space " + str(player2Square) + " to space " + str(player2NewSquare))

  player1Square = player1NewSquare
  player2Square = player2NewSquare

  turnNumber += 1
  input("Press Enter to continue.")
  print("")

for i in range(2):
  print("")
if player1Square == 100:
  cprint("Player 1 wins!", "red", attrs=['bold'])
if player2Square == 100:
  cprint("Player 2 wins!", "red", attrs=['bold'])