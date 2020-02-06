
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
    Creature.append(x.count("Creature"))
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
