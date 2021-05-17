
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

def printLevelOrder(root):
    if root is None:
        return 
    queue = []
    queue.append(root)
    while len(queue)>0:
        print(queue[0].data, end=' ')
        Root = queue.pop(0)
        if Root.left is not None:
            queue.append(Root.left)
        if Root.right is not None:
            queue.append(Root.right)

n = int(input())
root = node(n)
while True:
    n = int(input())
    if n == 0:
        break
    root.insertTree(n)
printLevelOrder(root)