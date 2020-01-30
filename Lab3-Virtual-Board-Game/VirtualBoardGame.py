import random
import numpy

#todo check what happens if string is used

gameOngoing = True
playerPositions = []
winner = 0
def checkSpace(player, space):
    if space == 199:
        #sends to spot one
        playerPositions[player] = 1
        print("Player " + str((player+1)) + "hit Spot 99 and was returned to spot 1")
    elif space % 13 == 0:
        #sends another random player to spot one
        playerToPunish = random.randint(0, players-1)
        print("Player " + str(player) + " landed on a multiple of 13")
        print("Player " + str(playerToPunish) + " was punished by being sent to spot 1")
        playerPositions[playerToPunish] = 1
    elif space % 10 == 0:
        #roll one die forward
        spacesMoved = random.randint(1,6)
        playerPositions[player] = playerPositions[player] + spacesMoved
        print("Player " + str((player+1)) + " gets to move forward one dice roll")
        print("They rolled a " + str(spacesMoved) + " and are now at " + str(playerPositions[player]))
    elif space % 7 == 0:
        #rolle one die backward
        spacesMoved = random.randint(1,6)
        playerPositions[player] = playerPositions[player] - spacesMoved
        print("Player " + str((player+1)) + " is punished with one dice roll back")
        print("They rolled a " + str(spacesMoved) + " and are now at " + str(playerPositions[player]))
    elif space % 4 == 0:
        #go back 3
        playerPositions[player] = playerPositions[player] - 3
        print("Player " + str((player+1)) + " got struck by unluckiness and sent back 3 spaces to " + str(playerPositions[player]))




players = int(input("How many players do you have? "))
while players <= 0:
    #verifies positive num of players
    print("There must be at least one player")
    players = input("How many players do you have? ")
for x in range(0, players):
    #creates array of locations of players (all start at 1)
    playerPositions.append(1)
while gameOngoing:
    for x in range(0, players):
        spacesMoved = random.randint(1,6) + random.randint(1,6)
        if spacesMoved == 2:
            #if snake eyes, loses turn
            print("Player " + str((x+1)) + " rolled snake eyes and loses their turn")
        else:
            #normal turn
            playerPositions[x] = playerPositions[x] + spacesMoved
            print("Player " + str((x+1)) + " moved forward " + str(spacesMoved) + " to spot " + str(playerPositions[x]))
            checkSpace(x, playerPositions[x])
        if playerPositions[x] > 200:
            gameOngoing = False
            winner = x+1
            break
print("The winner is Player " + str(winner))
