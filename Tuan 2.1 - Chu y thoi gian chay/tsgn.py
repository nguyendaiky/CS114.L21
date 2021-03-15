n= int(input())

arr = [int(x) for x in input().split()]

k,x = [int(x) for x in input().split()]

def binaryIndexLOE(left=0,right=n-1):
    if arr[left]>=x:
        return left
    if arr[right]<=x:
        return right
    
    pivot = (right+left)//2

    if arr[pivot] == x:
        return pivot

    if arr[pivot]>x:
        return binaryIndexLOE(left,pivot-1)
    else:
        if arr[pivot+1]>x:
            return pivot
        return binaryIndexLOE(pivot+1,right)
    

# linked list
class node :
    def __init__(self,value,nextnode=None):
        self.val = value
        self.next = nextnode
class list:
    def __init__(self,node=None):
        self.head=node
        self.tail=node

def printList(list):
    if list.head==None:
        return
    head = list.head

    while head.next != None:
        print(head.val,end=' ')
        head = head.next

    print(head.val)

def caseZero(list , val):
    new = node(val,list.head)
    list.head = new
    if new.next == None:
        list.tail = new
    return list

def caseOne(list, val):
    new = node(val)
    if list.head == None:
        list.head = new
        list.tail = new 
        return

    list.tail.next = new
    list.tail = new



indexLower = binaryIndexLOE()
indexHigher = indexLower+1

res = list()


if k>n:
    k=n
for i in range(k):
    if indexLower <0:
        caseOne(res,arr[indexHigher])
        indexHigher=indexHigher+1
    elif indexHigher>=n:
        caseZero(res,arr[indexLower])
        indexLower = indexLower-1
    else:
        if (x-arr[indexLower])<=(arr[indexHigher]-x):
            caseZero(res,arr[indexLower])
            indexLower = indexLower-1
        else:
            caseOne(res,arr[indexHigher])
            indexHigher=indexHigher+1

printList(res)