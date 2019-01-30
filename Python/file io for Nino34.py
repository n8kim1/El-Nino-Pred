outlist = []

infile = open("Nino34.txt", "r")
inString = infile.read()
while len(inString) > 0:
    element = ""
    while len(inString) > 0 and inString[0] != "\n":
        element += inString[0]
        inString = inString[1:]
    outlist.append(round(float(element)-24,2))
    inString = inString[1:]
infile.close()
