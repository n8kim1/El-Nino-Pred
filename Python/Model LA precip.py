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
inList = [8.52, 6.08, 5.85, 8.69, 20.2, 16.36, 9.08, 13.53]
realList = [8.52, 6.08, 5.85, 8.69, 20.2, 16.36, 9.08, 13.53, 3.21, 13.19, 37.96, 9.25, 16.42, 4.42, 17.94, 11.57, 9.09, 31.01, 12.4, 12.44, 24.35, 8.11, 27.36, 21.0, 11.99, 7.35, 8.08, 12.48, 7.66, 17.86, 12.82, 10.43, 31.28, 10.71, 8.96, 26.98, 19.67, 33.44, 12.3, 7.21, 14.35, 14.92, 21.26, 7.17, 12.32, 7.74, 27.47, 16.58, 22.0, 20.44, 13.68, 7.93, 8.38, 18.79, 4.85, 8.18, 5.58, 21.13, 9.54, 16.0, 11.94, 11.99, 9.46, 26.21, 8.21, 10.59, 7.99, 7.22, 12.36, 11.65, 11.59, 19.22, 18.17, 11.18, 32.76, 19.21, 13.07, 23.43, 22.41, 13.47, 21.66, 14.94, 11.88, 16.93, 12.52, 11.52, 12.66, 9.77, 18.03, 17.56, 7.94, 6.67, 9.59, 19.66, 13.65, 12.52, 8.58, 13.86, 15.26, 19.92, 17.05, 23.65, 13.42, 11.6, 16.18, 12.63, 19.18, 11.72, 19.3, 18.65, 19.52, 8.72, 19.32, 10.6, 16.29, 7.91, 5.59, 7.06, 18.83, 8.51, 16.11, 6.73, 26.28, 11.85, 13.36, 34.84, 19.28, 13.87, 14.05, 22.31, 9.21, 38.18, 12.16]
testList = [10.4, 13.13, 20.34, 11.35, 21.26]
newTerms = len(realList) - len(inList)
swapsPer = 5
mutationsPer = 5
gensDef = 1000

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
