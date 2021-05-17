import io,os,sys
import collections
input = sys.stdin.readline
out = collections.deque()

while True:
    arr = list(map(int,input().split()))
    if arr[0] == 3:
        break
    elif arr[0] == 0:
        out.appendleft(arr[1])
    elif arr[0] == 1:
        out.append(arr[1])
    elif arr[0] == 2:
        if arr[1] in out:
            out.insert(out.index(arr[1])+1, arr[2])
        else:
            out.appendleft(arr[2])

class node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
    
def insert(root,val):
    if root is None:
        return node(val)
    else:
        if root.data == val:
            return root
        elif root.data > val:
            root.left = insert(root.left, val)
        elif root.data < val:
            root.right = insert(root.right, val)
    return root
    
def heightOfTree(root):
    if root is None:
        return 0
    else:
        l = heightOfTree(root.left)
        r = heightOfTree(root.right)
        return max(l,r)+1
    
root = None
for i in out:
    root = insert(root, i)
print(heightOfTree(root))