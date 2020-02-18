import matplotlib
import matplotlib.pyplot as plt

def setupChart():
    plt.clf()
    plt.xlabel(r"$Chapter(Letters1-4)$")
    plt.ylabel(r"$Mentions$")
    plt.ylim(0, 20)
    plt.xlim(0, 29)

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

plt.figure()
setupChart()
plt.bar(list(range(1,29)), Victor) #1 to 28 for each chapter including the letters
plt.savefig("Victor.png", format="png")
setupChart()
plt.bar(list(range(1,29)), Creature)
plt.savefig("Creature.png", format="png")
setupChart()
plt.bar(list(range(1,29)), Agatha)
plt.savefig("Agatha.png", format="png")
setupChart()
plt.bar(list(range(1,29)), Caroline)
plt.savefig("Caroline.png", format="png")
setupChart()
plt.bar(list(range(1,29)), De_Lacey)
plt.savefig("De_Lacey.png", format="png")
setupChart()
plt.bar(list(range(1,29)), Elizabeth)
plt.savefig("Elizabeth.png", format="png")
setupChart()
plt.bar(list(range(1,29)), Ernest)
plt.savefig("Ernest.png", format="png")
setupChart()
plt.bar(list(range(1,29)), Felix)
plt.savefig("Felix.png", format="png")
setupChart()
plt.bar(list(range(1,29)), Henry)
plt.savefig("Henry.png", format="png")
setupChart()
plt.bar(list(range(1,29)), Justine)
plt.savefig("Justine.png", format="png")
setupChart()
plt.bar(list(range(1,29)), William)
plt.savefig("William.png", format="png")

#Characters who appear in the same chapters (meet):

#(5)	Caroline, Creature, Elizabeth, Victor
#(6)	Elizabeth, Henry, Victor
#(10)	Creature, Elizabeth, Earnest, Justine, Victor, William
#(11)	Caroline, Creature, Elizabeth, Earnest, Henry, Justine, Victor, William
#(16)	Agatha, Creature
#(17)	Agatha, Creature, Felix
#(18)	Agatha, DeLacey, Felix
#(19)	Agatha, Creature, DeLacey, Felix

#Characters who do not meet:

#Agatha: Earnest, Elizabeth, Henry, Justine, Victor, William
#Caroline: Agatha, DeLacey, Felix
#DeLacey: Elizabeth, Earnest, Henry, Justine, Victor, William

#Characters who either die or are not mentioned again in the script:

#Agatha, Caroline, DeLacey, Henry
