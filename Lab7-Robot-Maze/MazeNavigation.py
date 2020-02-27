import numpy
import random as rand

class Robot:
    historyRow = []
    historyCol = []
    currentCol = 0
    currentRow = 0
    facing = 2
    def __init__(self, startCol, startRow):
        self.currentCol = startCol
        self.currentRow = startRow
    def move(self):
        times = 0
        while times < 5:
            col = self.currentCol;
            row = self.currentRow;
            if self.facing is 0:
                row = row - 1
            elif self.facing is 1:
                col = col + 1
            elif self.facing is 2:
                row = row + 1
            elif self.facing is 3:
                col = col - 1
            i = 0
            while i < len(self.historyCol):
                if col is self.historyCol[i] and row is self.historyRow[i]:
                    self.hitWall()
                    break
                i = i + 1
            break
        self.historyCol.append(self.currentCol)
        self.historyRow.append(self.currentRow)
        return self.facing
    def hitWall(self):
        self.facing = self.facing + 1
        if self.facing > 3:
            self.facing = self.facing % 4

def makeMove(direction, robot):
    col = robot.currentCol;
    row = robot.currentRow;
    if direction is 0:
        row = row - 1
    elif direction is 1:
        col = col + 1
    elif direction is 2:
        row = row + 1
    elif direction is 3:
        col = col - 1
    if map[row][col] is '#':
        robot.hitWall()
    elif map[row][col] is '_' or map[row][col] is 'S':
        robot.currentCol = col;
        robot.currentRow = row;
    elif map[row][col] is 'G':
        return False
    return True


boardFile = open("Map3.map","r")                    #change board here
map = [[],[]]
gameRunning = True
startingPositions = 0
i = 0
for line in boardFile:
    for character in line:
        if character is 'S':
            startingPositions = startingPositions + 1
        map[i].append(character)
    map[i] = map[i][:-1]
    map.append([])
    i = i + 1
map = map[:-2]

startingRow = 0
startingCol = 0
goalCol = 0
goalRow = 0
targetStart = rand.randint(1, startingPositions)
for j in range(len(map)):
    for i in range(len(map[j])):
        if map[j][i] is 'S':
            targetStart = targetStart - 1
            if targetStart is 0:
                startingCol = i
                startingRow = j

testBot = Robot(startingCol, startingRow)
turns = 0
while gameRunning:
    map[testBot.currentRow][testBot.currentCol] = '_'
    turns = turns + 1
    gameRunning = makeMove(testBot.move(), testBot)
    map[testBot.currentRow][testBot.currentCol] = 'R'
    print("Turn", turns)
    print(*map, sep = "\n")
print("Your bot took ", turns, "turns")
