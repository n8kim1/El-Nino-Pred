class BTree:
    def __init__ (self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__ (self, value, children = []):
        self.value = value
        self.children = children

    def __leafmult__ (self):
        p = 1
        for i in range (0, len(self.children)):
            if len(self.children[i].children) == 0:
                p *= self.children[i].value
            else:
                p *= self.children[i].__leafmult__()
        return p

    def __recmult__ (self):
        p = 1
        for i in range (0, len(self.children)):
            if len(self.children[i].children) == 0:
                p *= self.children[i].value
            else:
                p *= self.children[i].value * self.children[i].__recmult__()
        return p

    def __addChild__ (self, child):
        self.children.append(child)

def swap (a, b): # use: a, b = swap (a, b)
    return b, a

a = Tree (1)
b = Tree (2)

c = Tree (3)
d = Tree (4)
e = Tree (5)

x = Tree (6, [a, b])
y = Tree (7, [c, d, e])
z = Tree (1, [x, y])
