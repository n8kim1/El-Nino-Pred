# need depth limit

import random

# bunch of global vars
nodes = 0
leaves = 0
toPrint = []
toPrintList = []
nodeList = []
leafList = []
index2 = 0
fn = []
fnList = []
evalList = []
accList = []
accGen = []
fnGen = []

# constants

minLeaves = 180 # 90
maxLeaves = 220 # 110
opList = ["+", "-", "*", "/"]
maxDepth = 10 # 10
#inList = [15.36, 8.53, 9.61, 18.72, 0.66, 0.39, 4.93, 2.57]
#realList = [15.36, 8.53, 9.61, 18.72, 0.66, 0.39, 4.93, 2.57, -0.11, 9.06, 12.59, 13.2, 4.54, 13.2, 9.39, 17.25, 3.97, -5.57, -4.16, 5.1, 10.09, 10.1, 22.23, 8.27, 8.51, 12.18, 6.33, 1.16, -9.86, 2.47, -3.7, -8.6, 1.49, -2.18, 8.11, -9.21, 3.04, 7.48, -5.56, -4.4, -15.18, -6.72, -7.46, -14.99, -7.84, -7.23, -5.65, -10.97, -1.74, -7.81, -6.92, -5.67, -7.04, -13.06, 2.82, -1.45, -2.05, -2.21, -3.12, 9.78, -11.86, 9.26, 0.93, -15.84, 12.77, -15.3, -7.11, -7.67, -2.99, -3.42, -8.54, -8.24, 1.97, -28.68, -0.11, -11.39, -14.03, 2.3, 1.22, -7.25, 3.46, 10.67, -2.59, 0.07, 12.92, 0.13, 14.12, 14.5, -9.26, -6.34, -9.69, -14.95, -5.14, -15.62, -1.06, -3.53, -7.79, -2.4, -1.13, -3.54, -3.33, 5.65, -4.57, 2.19, 1.61, 5.94, 9.63, 14.68, 13.97, 21.38, 12.37, 4.87, -4.5, 4.9, 2.06, 8.66, 13.51, 13.23, 17.15, 13.26, 9.11, 14.92, 0.14, 8.77, -5.53, -2.09, 1.78, -4.45, 3.45, -14.6, -6.74, -7.22, -9.52, -15.37, -11.08, 14.44, 9.98, 2.43, 20.08, 18.22, 25.52, 18.2, 16.42, 27.03, 19.97, 22.56, 21.29, 25.73, 1.72, 1.58, 10.37, 2.03, 11.42, 8.37, 12.99, 22.98, 9.88, 2.37, 2.92, -6.53, -2.74, -10.73, -1.03, -5.72, 2.88, 2.18, 3.92, -6.13, -0.29, -3.8, 11.0, 0.66, 7.82, 13.25, 7.78, -0.53, 4.66, -2.26, 9.89, 0.47, 12.3, -1.21, -13.13, 8.09, 4.26, -1.2, -3.35, -11.51, -6.98, -7.8, -9.54, -5.77, -7.8, 0.54, -11.28, -3.4, -14.05, -11.85, -14.84, -20.14, -17.14, -20.1, -4.57, -1.85, -20.29]
#testList = [-17.14, -20.1, -4.57, -1.85, -20.29]
#newTerms = len(realList) - len(inList)
swapsPer = 5
mutationsPer = 5
gensDef = 1000



outlist = []

infile = open("Nino34.txt", "r")
inString = infile.read()
while len(inString) > 0:
    element = ""
    while len(inString) > 0 and inString[0] != "\n":
        element += inString[0]
        inString = inString[1:]
    outlist.append(round((float(element)-24)*8,2))
    inString = inString[1:]
infile.close()

inList = outlist[:8]
realList = outlist[:-5]
testList = outlist[-5:]
newTerms = len(realList) - len(inList)

# class definitions

class Node:
    
    def __init__ (self, operation, value, depth, parent, children, index):
        self.operation = operation
        self.value = value
        self.children = children
        self.depth = depth
        self.parent = parent
        self.index = index

    def isleaf (self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def makeRoot (self):
        global nodes
        global leaves
        global toPrint
        global nodeList
        global leafList
        global index2
        global fn
        global fnList
        global maxDepth
        
        # initialize stuff

        nodes = 0
        leaves = 0
        toPrint = []
        nodeList = []
        leafList = []
        index2 = 0
        fn = []
        fnList = []
    
        nodeList.append(self)
        nodes += 1
        index2 += 1
        rootChildren = random.randint(1, 2)
        for i in range (0, rootChildren):
            if self.depth < maxDepth:
                op = opList[random.randint(0, len(opList))-1]
                if random.randint(0, 9) > 7:
                    val = str(4*random.random() - 2)
                else:
                    j = str(random.randint(1, 8))
                    val = "inListCopy[t-" + j + "]"
                x = Node (op, val, self.depth+1, self, [], index2)
                x.makeChildren ()
                self.children.append(x)
                

    def makeChildren(self):
        global nodes
        global leaves
        global nodeList
        global index2
        global maxDepth

        nodeList.append(self)
        nodes += 1
        index2 += 1
        n = random.randint(0, 3)
        if n == 0:
            # leaf
            leaves += 1
            leafList.append(self)
        else:
            if self.depth < maxDepth:
                for i in range (0, n):
                    op = opList[random.randint(0, len(opList))-1]
                    if random.randint(0, 9) > 7:
                        val = str(4*random.random() - 2)
                    else:
                        j = str(random.randint(1, 8))
                        val = "inListCopy[t-" + j + "]"
                    x = Node (op, val, self.depth+1, self, [], index2)
                    x.makeChildren()
                    self.children.append(x)
            else:
                # no children generated --> leaf
                leaves += 1
                leafList.append(self)

    def printTree (self):
        global toPrint

        # set to [] before call
        global toPrintList
        
        # finds every path down a tree and prints it
        toPrint.append(self.index)
        if self.isleaf():
            toPrintList.append(toPrint)
            toPrint = toPrint[:-1]
        else:
            for i in range (0, len(self.children)):
                self.children[i].printTree()
            toPrint = toPrint[:-1]

    def getFns (self):
        # gets a list of all functions
        # similar to printTree
        global fn

        # set to [] before call
        global fnList
        
        # finds every path down a tree and prints it
        fn.append(self.operation)
        fn.append(self.value)
        if self.isleaf():
            fnList.append("".join(fn))
            fn = fn[:-2]
        else:
            for i in range (0, len(self.children)):
                self.children[i].getFns()
            fn = fn[:-2]

    def findNode (self, index):
        # returns a node with a given index
        if index == self.index:
            return self
        else:
            for i in range (0, len(self.children)):
                if self.children[i].findNode(index) != None:
                    return self.children[i].findNode(index)

    def update (self, parent, depth):
        # reupdates parent, depth, and index of each leaf, starting at root
        # also recounts nodes and leaves

        # set to 0 before call
        global index2
        global nodes
        global leaves
        # set to [] before call
        global nodeList
        global leafList

        # update parent
        self.parent = parent

        # update depth
        self.depth = depth

        # update index
        self.index = index2
        index2 += 1

        # update nodes, nodeList
        nodes += 1
        nodeList.append(self)

        # update leaves
        if self.isleaf():
            leaves += 1
            leafList.append(self)
        
        # recursion
        for i in range (0, len(self.children)):
            self.children[i].update(self, self.depth + 1)

    def killBranch (self, child = None):
        # given the index of a node, kills the branch

        # first, travel up to the start of the branch
        if len(self.children) < 2:
            self.parent.killBranch(self)

        # remove from children
        else:
            self.children.remove(child)

        # update tree after!

    def duplicate (self, attachTo = None):
        # duplicates branch, starting at top
        newNode = Node (self.operation, self.value, self.depth, self.parent, self.children, -1)
        newNode.children = []
        if attachTo == None:
            self.parent.children.append(newNode)
        else:
            attachTo.children.append(newNode)
        if not self.isleaf():
            self.children[0].duplicate(newNode)
        # update after!

    def topBranch (self):
        # finds top of branch, given leaf
        if len(self.parent.children) > 1:
            return self
        else:
            return self.parent.topBranch()

    def swap (self, node1, node2):
        # swaps the position of two nodes
        # more specifically, changes the children list of each parent
        # be sure to check that both nodes are deep enough
        # make sure that either node isn't in the other's subtree,
        # or that they are not siblings (i.e. share same parent)

        node3 = node1.parent
        node4 = node2.parent
        if node1.depth < 7 or node2.depth < 7:
            return 2 # failed
        if node1.findNode(node2.index) == None and node2.findNode(node1.index) == None:
            node3.children[node3.children.index(node1)] = node2
            node4.children[node4.children.index(node2)] = node1
            return 0 # success!
        else:
            return 1 # failed
        # update after!

    def addNode(self):
        # adds a random new node to self

        global maxDepth
        
        if self.depth == maxDepth:
            return 1 # failed
        else:
            op = opList[random.randint(0, len(opList))-1]
            if random.randint(0, 9) > 7:
                val = str(4*random.random() - 2)
            else:
                j = str(random.randint(1, 8))
                val = "inListCopy[t-" + j + "]"
            newNode = Node (op, val, self.depth+1, self, [], -1)
            self.children.append(newNode)
        # update after!

    def changeNode(self):
        # randomly changes self

        if self.depth < 5:
            return 1 # fail
        else:
            op = opList[random.randint(0, len(opList))-1]
            if random.randint(0, 9) > 7:
                val = str(4*random.random() - 2)
            else:
                j = str(random.randint(1, 8))
                val = "inListCopy[t-" + j + "]"
            self.operation = op
            self.value = val
            return 0 # success!

##        op = opList[random.randint(0, len(opList))-1]
##        if random.randint(0, 1) == 0:
##            val = str(4*random.random() - 2)
##        else:
##            j = random.randint(1, 4)
##            if j == 1:
##                val = "inListCopy[t-1]"
##            elif j == 2:
##                val = "inListCopy[t-2]"
##            elif j == 3:
##                val = "inListCopy[t-3]"
##            else:
##                val = "inListCopy[t-4]"
##        self.operation = op
##        self.value = val
##        return 0 # success!
    
# convenience functions

def updateRoot():
    global nodes
    nodes = 0
    global leaves
    leaves = 0
    global index2
    index2 = 0
    global nodeList
    nodeList = []
    global leafList
    leafList = []
    root.update(None, 0)
    
def printRoot():
    global toPrintList
    toPrintList = []
    root.printTree()
    return toPrintList

def fnRoot():
    global fnList
    fnList = []
    root.getFns()
    return fnList

def evalFns():
    global evalList
    fnRoot()
    evalList = []
    for i in range (0, len(fnList)):
        inListCopy = []
        inListCopy2 = []
        for k in range (0, len(inList)):
            inListCopy.append(inList[k])
            inListCopy2.append(inList[k])
        for j in range (0, newTerms):
            t = len(inList) + j
            try:
                inListCopy2.append(eval(fnList[i]))
            except:
                #print("ZeroDivisionError detected.")
                inListCopy2.append(1000000000)
            inListCopy.append(realList[t])
        evalList.append(inListCopy2)
    #print(evalList)

def accFns():
    # compute RMSE of each function
    global evalList
    global accList
    evalFns()
    accList = []
    for i in range (0, len(evalList)):
        rmse = 0
        fn = evalList[i]
        for j in range (len(inList), len(inList) + newTerms):
            try:
                percentAcc = abs(100* (fn[j] - realList[j]) / realList[j])
                #rmse += (percentAcc)**2
                rmse += percentAcc
            except OverflowError:
                #print("OverflowError detected.")
                rmse += 1000000000
                #print(rmse)
        #rmse = (rmse / newTerms) ** 0.5
        rmse = rmse / newTerms
        accList.append(rmse)

def killModels():
    # kill a specified number of models
    accFns()
    global accList
    global leafList
    global leaves
    #for i in range (0, kills):
    for i in range (0, int(leaves/2)):
        j = accList.index(max(accList))
        accList.pop(j)
        leafList[j].killBranch()
        leafList.pop(j)
    updateRoot()

def duplicateModels():
    # duplicates a specified number of models
    accFns()
    global accList
    global leafList
    global leaves
    accList2 = []
    for i in range (0, len(accList)):
        accList2.append(accList[i])
    for i in range(0, int(leaves * 0.9)):
        j = accList.index(min(accList2))
        leafList[j].duplicate()
        accList2.remove(min(accList2))
        if i + leaves > maxLeaves:
            break
    updateRoot()

def newModels():
    # creates a specified number of models
    global leaves
    global nodeList
    global maxLeaves
    for i in range (0, int(leaves * 0.5)):
        j = random.randint(1, len(nodeList)-1)
        nodeList[j].addNode()
        if i + leaves > maxLeaves:
            break
    updateRoot()

def swapModels():
    # carries out a specified number of SUCCESSFUL swaps
    global nodeList
    for i in range (0, swapsPer):
    # for i in range (0, 3):
        j = random.randint(1, len(nodeList)-1)
        k = random.randint(1, len(nodeList)-1)
        result = root.swap(nodeList[j], nodeList[k])
        failCount = 0
        while result != 0 and failCount < 20:
            failCount += 1
            j = random.randint(1, len(nodeList)-1)
            k = random.randint(1, len(nodeList)-1)    
            result = root.swap(nodeList[j], nodeList[k])
        updateRoot()


def mutateModels():
    # carries out a specified number of SUCCESSFUL mutations
    global nodeList
    for i in range (0, mutationsPer):
        j = random.randint(1, len(nodeList)-1)
        result = nodeList[j].changeNode()
        failCount = 0
        while result != 0 and failCount < 20:
            failCount += 1
            j = random.randint(1, len(nodeList)-1)
            result = nodeList[j].changeNode()
        updateRoot()



def simGen():
    # simulates a generation
    killModels()
    duplicateModels()
    newModels()
    swapModels()
    mutateModels()
    updateRoot() # for good measure

def simGens(gens = gensDef):
    # simulates many generations
    for i in range (0, gens):
        simGen()
        accFns()
        accGen.append(min(accList))
        j = accList.index(min(accList))
        fnGen.append(fnList[j])
        if i % max(int(gens/10), 1) == 0:
            print(i)

    # POP NAN

def testModel():
    gen = accGen.index(min(accGen))
    print(gen)
    fn = fnGen[gen]
    inListCopy = []
    #inListCopy2 = []
    testList2 = []
    for i in range (0, len(realList)):
        inListCopy.append(realList[i])
        #inListCopy2.append(realList[i])
    for j in range (0, len(testList)):
        t = len(realList) + j
        try:
            #inListCopy2.append(eval(fn))
            testList2.append(eval(fn))
        except:
            #inListCopy2.append(1000000000)
            testList2.append(eval(1000000000))
        inListCopy.append(testList[j])
    print(testList2)
    # compare testList and testList2
    rmse = 0
    for k in range (0, len(testList)):
        try:
            percentAcc = abs(100* (testList2[k] - testList[k]) / testList[k])
            rmse += percentAcc
        except OverflowError:
            rmse += 1000000000
    rmse = rmse / len(testList)
    return rmse
            
# building the tree
root = Node ("", "1", 0, None, [], 0)
root.makeRoot()
while maxLeaves < leaves or minLeaves > leaves:
    # try again
    root = Node ("", "1", 0, None, [], 0)
    root.makeRoot()

# INITIAL MODEL DONE

#root.printTree()
#print(toPrintList)
