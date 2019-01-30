outlist = []

infile = open("LAPrecip.txt", "r")
inString = infile.read()
while len(inString) > 0:
    element = ""
    while len(inString) > 0 and inString[0] != "\n":
        element += inString[0]
        inString = inString[1:]
    outlist.append(float(element))
    inString = inString[1:]
infile.close()
