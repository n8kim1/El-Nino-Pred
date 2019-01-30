# need depth limit

import random;

# why this works, I don't know.  DON'T CHANGE
nodes = 0
leaves = 0
toPrint = []
toPrintList = []
nodeList = []

# limits

minLeaves = 90
maxLeaves = 110

# class definitions

class Node:


    maxDepth = 10 # change as necessary
    
    def __init__ (self, operation, value, depth, children = []):
        self.operation = operation
        self.value = value
        self.children = []
        self.depth = depth

    def isleaf (self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def makeRoot (self):
        global nodes
        global nodeList
        
        nodeList.append(self)
        nodes += 1
        rootChildren = random.randint(1, 2)
        for i in range (0, rootChildren):
            if self.depth < self.maxDepth:
                x = Node ("", nodes, self.depth+1)
                x.makeChildren ()
                self.children.append(x)
                

    def makeChildren(self):
        global nodes
        global leaves
        global nodeList

        nodeList.append(self)
        nodes += 1
        n = random.randint(0, 3)
        if n == 0:
            # leaf
            leaves += 1
        else:
            if self.depth < self.maxDepth:
                for i in range (0, n):
                    x = Node ("", nodes, self.depth+1)
                    x.makeChildren()
                    self.children.append(x)
            else:
                # no children generated --> leaf
                leaves += 1

    def printTree (self):
        global toPrint
        global toPrintList
        
        # finds every path down a tree and prints it
        toPrint.append(self.value)
        if self.isleaf():
            toPrintList.append(toPrint)
            # print("hi ", toPrintList)
            # print ("help " , toPrint)
            toPrint = toPrint[:-1]
        else:
            for i in range (0, len(self.children)):
                self.children[i].printTree()
            toPrint = toPrint[:-1]

# building the tree

root = Node ("", nodes, 0)
root.makeRoot()
while maxLeaves < leaves or minLeaves > leaves:
##    print(leaves)
##    print("again")
    # try again
    nodes = 0
    leaves = 0
    toPrint = []
    nodeList = []
    root = Node ("", nodes, 0)
    root.makeRoot()

# INITIAL MODEL DONE

root.printTree()
print(toPrintList)
print(leaves)
