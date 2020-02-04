
chapters = [[],[]]
i = 0
frankensteinText = open("Frankenstein.txt", "r")
#creates 2D array of chapter with lines of text
for line in frankensteinText:
    if ("Chapter") in line:
        i = i + 1
        chapters.append([])
    if ("Letter") in line:
        i = i + 1
        chapters.append([])
    chapters[i].append(line)
frankensteinText.close()
del chapters[:29] #removes all the table of contents
