
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
print(chapters[0])
