n = int(input())
A = [int(i) for i in input().split()]
k, x = [int(i) for i in input().split()]

def Search(left,right,x):
    if x <= A[left]:
        return left
    if x >= A[right]:
        return right

    pivot = (left+right)//2

    if x == A[pivot]:
        return pivot
    elif x < A[pivot]:
        return Search(left,pivot-1,x)
    elif x > A[pivot]:
        return Search(pivot+1,right,x)

left = 0
right = n-1
indexLeft = Search(left,right,x)
indexRight = indexLeft + 1

class node:
    def __init__(self,val,nextNode=None):
        self.value = val
        self.next = nextNode

class list:
    def __init__(self):
        self.head = None
        self.tail = None

    def headAppend(self,val):
        new = node(val)
        new.next = self.head
        self.head = new
        if self.head.next == None:
            self.tail = new
        
    def tailAppend(self,val):
        new = node(val)
        self.tail.next = new
        self.tail = new

    def printList(self):
        if self.head == None:
            return
        t = self.head
        while t.next != None:
            print(t.value, end=' ')
            t = t.next
        print(t.value, end=' ')
            

ans = list()
for i in range(k):
    if indexLeft < 0:
        ans.tailAppend(A[indexRight])
        indexRight += 1
    elif indexRight >= n:
        ans.headAppend(A[indexLeft])
        indexLeft -= 1
    else:
        if (x - A[indexLeft]) <= (A[indexRight] - x):
            ans.headAppend(A[indexLeft])
            indexLeft -= 1
        else:
            ans.tailAppend(A[indexRight])
            indexRight += 1
    
ans.printList()


    