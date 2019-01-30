# need depth limit

import random

# why this works, I don't know.  DON'T CHANGE
nodes = 0
leaves = 0
toPrint = []
toPrintList = []
nodeList = []
leafList = []
index2 = 0

# constants

minLeaves = 5 # 90
maxLeaves = 10 # 110
opList = ["+", "-", "*", "/"]

# class definitions

class Node:


    maxDepth = 10 # change as necessary
    
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
        global nodeList
        global index2
        
        nodeList.append(self)
        nodes += 1
        index2 += 1
        rootChildren = random.randint(1, 2)
        for i in range (0, rootChildren):
            if self.depth < self.maxDepth:
                op = opList[random.randint(0, len(opList))-1]
                val = 4*random.random() - 2
                x = Node (op, val, self.depth+1, self, [], index2)
                x.makeChildren ()
                self.children.append(x)
                

    def makeChildren(self):
        global nodes
        global leaves
        global nodeList
        global index2

        nodeList.append(self)
        nodes += 1
        index2 += 1
        n = random.randint(0, 3)
        if n == 0:
            # leaf
            leaves += 1
            leafList.append(self)
        else:
            if self.depth < self.maxDepth:
                for i in range (0, n):
                    op = opList[random.randint(0, len(opList))-1]
                    val = 4*random.random() - 2
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
        global fnList

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
        

        # update nodeList
        nodeList.append(self)
        
        # recursion
        for i in range (0, len(self.children)):
            self.children[i].update(self, self.depth + 1)

    def killBranch (self, child):
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
        newNode = Node (self.operation, self.value, self.depth, self.parent, self.children, self.index)
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
        elif node1.findNode(node2.index) == None and node2.findNode(node1.index) == None:
            node3.children[node3.children.index(node1)] = node2
            node4.children[node4.children.index(node2)] = node1
        else:
            return 1 # failed
        # update after!

    def addNode(self):
        # adds a random new node to self

        if self.depth == self.maxDepth:
            return 1 # failed
        else:
            newNode = Node("", 0, self.depth+1, self, [], 0)
            self.children.append(newNode)
        # update after!

    def changeNode(self):
        # randomly changes self

        if self.depth < 5:
            self.operation = "changeMe"
            self.value = 100
    
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
    root.update(None, 0)
    
def printRoot():
    global toPrintList
    toPrintList = []
    root.printTree()
    print(toPrintList)

# building the tree
root = Node ("", 1, 0, None, [], 0)
root.makeRoot()
while maxLeaves < leaves or minLeaves > leaves:
##    print(leaves)
##    print("again")
    # try again
    nodes = 0
    leaves = 0
    toPrint = []
    nodeList = []
    leafList = []
    index2 = 0
    root = Node ("", nodes, 0, None, [], 0)
    root.makeRoot()

# INITIAL MODEL DONE

root.printTree()
print(toPrintList)
