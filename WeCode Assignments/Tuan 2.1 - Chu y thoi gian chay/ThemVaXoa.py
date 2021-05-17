import io,os,sys
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import time
class node:
    def __init__(self, val, nextNode = None):
        self.value = val
        self.next = nextNode 

class listNode:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def appendHead(self, val):
        new = node(val)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head = new

    def appendTail(self, val):
        new = node(val)
        if self.head is None:
            self.head = self.tail = None
        else:
            self.tail.next = new
            self.tail = new

    def find(self,x):
        p = self.head 
        while p is not None:
            if p.value == x:
                return p
            p = p.next
        return None

    def insert(self, a, b):
        p = find(a)
        if p is None:
            self.appendHead(b)
        else:
            t = node(b)
            t.next = p.next 
            p.next = t 
 
    def deleteOne(self,n):
        if self.head is None:
            return
        if self.head.value == n:
            p = self.head
            self.head = p.next
            del p 
        temp = self.head
        while temp.next is not None:
            if temp.next.value == n:
                p = temp.next
                temp.next = temp.next.next
                del p
                break
            temp = temp.next
        
    def deletaAll(self,n):
        if self.head is None:
            return
        if self.head.value == n:
            p = self.head
            self.head = p.next
            del p
            if self.head is None:
                return
        temp = self.head
        previous = temp
        while temp is not None:
            if temp.value == n:
                previous.next = temp.next
                del temp
                temp = previous.next
            else:
                previous = temp
                temp = temp.next
            
        
    def deleteHead(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            p = self.head 
            self.head = self.tail = None 
            del p 
        else:
            p = self.head 
            self.head = self.head.next
            del p 

    def printList(self):
        if self.head is None:
            print('blank')
        else:
            p = self.head
            ans = []
            while p is not None:
                ans.append(p.value)
                p = p.next
        sys.stdout.write(" ".join(map(str,ans)) + "\n")

ans = listNode()
while True:
    arr = ([int(i) for i in input().split()])
    T = arr[0]
    if T == 0:
        ans.appendHead(arr[1])
    elif T == 1:
        ans.appendTail(arr[1])
    elif T == 2:
        ans.insert(arr[1],arr[2])
    elif T == 3:
        ans.deleteOne(arr[1])
    elif T == 4:
        ans.deletaAll(arr[1])
    elif T == 5:
        ans.deleteHead()
    elif T == 6:
        ans.printList()
        break
