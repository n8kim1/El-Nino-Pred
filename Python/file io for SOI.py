outlist = []

infile = open("SOI.txt", "r")
inString = infile.read()
while len(inString) > 0:
    element = ""
    while len(inString) > 0 and inString[0] != "\n":
        element += inString[0]
        inString = inString[1:]
    outlist.append(round(float(element)+30,2))
    inString = inString[1:]
infile.close()
