import matplotlib
import matplotlib.pyplot as ptl

def setupChart():
    ptl.clf()
    ptl.xlabel(r"$Chapter(Letters1-4)$")
    ptl.ylabel(r"$Mentions$")
    ptl.ylim(0, 20)
    ptl.xlim(0, 29)

chapters = [""]
i = 0
frankensteinText = open("Frankenstein.txt", "r")
#creates 2D array of chapter with lines of text
for line in frankensteinText:
    if ("Chapter") in line:
        i = i + 1
        chapters.append(line)
    elif ("Letter") in line:
        i = i + 1
        chapters.append(line)
    else:
        chapters[i] = chapters[i] + line
frankensteinText.close()
del chapters[:29] #removes all the table of contents
Victor = []
Creature = []
Agatha = []
Caroline = []
De_Lacey = []
Elizabeth = []
Ernest = []
Felix = []
Henry = []
Justine = []
William = []

for x in chapters:
    Victor.append(x.count("Victor"))
    Creature.append(x.count("creature"))
    Agatha.append(x.count("Agatha"))
    Caroline.append(x.count("Caroline"))
    De_Lacey.append(x.count("De Lacey"))
    Elizabeth.append(x.count("Elizabeth"))
    Ernest.append(x.count("Ernest"))
    Felix.append(x.count("Felix"))
    Henry.append(x.count("Henry"))
    Justine.append(x.count("Justine"))
    William.append(x.count("William"))
print("Victor: " + str(Victor))
print("Creature: " + str(Creature))
print("Agatha: " + str(Agatha))
print("Caroline: " + str(Caroline))
print("De_Lacey: " + str(De_Lacey))
print("Elizabeth: " + str(Elizabeth))
print("Ernest: " + str(Ernest))
print("Felix: " + str(Felix))
print("Henry: " + str(Henry))
print("Justine: " + str(Justine))
print("William: " + str(William))

ptl.figure()
setupChart()
ptl.bar(list(range(1,29)), Victor) #1 to 28 for each chapter including the letters
ptl.savefig("Victor.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), Creature)
ptl.savefig("Creature.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), Agatha)
ptl.savefig("Agatha.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), Caroline)
ptl.savefig("Caroline.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), De_Lacey)
ptl.savefig("De_Lacey.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), Elizabeth)
ptl.savefig("Elizabeth.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), Ernest)
ptl.savefig("Ernest.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), Felix)
ptl.savefig("Felix.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), Henry)
ptl.savefig("Henry.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), Justine)
ptl.savefig("Justine.png", format="png")
setupChart()
ptl.bar(list(range(1,29)), William)
ptl.savefig("William.png", format="png")
