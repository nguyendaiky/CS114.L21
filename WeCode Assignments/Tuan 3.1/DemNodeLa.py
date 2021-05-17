
class node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def insertTree(self,val):
        if self.data:
            if val < self.data:
                if not self.left:
                    self.left = node(val)
                else:
                    self.left.insertTree(val)
            elif self.data < val:
                if not self.right:
                    self.right = node(val)
                else:
                    self.right.insertTree(val)
        else:
            self.data = val
    
    def countLeafTree(self):
        if self.data:
            if (not self.left) and (not self.right):
                return 1
            else:
                if not self.left:
                    return self.right.countLeafTree()
                elif not self.right:
                    return self.left.countLeafTree()
                elif self.right and self.left:
                    return self.left.countLeafTree() + self.right.countLeafTree()
        else:
            return 0

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=' ')
        if self.right:
            self.right.printTree()

n = int(input())
root = node(n)
while True:
    n = int(input())
    if n == 0:
        break
    root.insertTree(n)
#root.printTree()
print(root.countLeafTree())