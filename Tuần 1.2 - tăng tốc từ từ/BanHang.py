import math 
a = int(input())
for i in range(a):
    n = int(input())
    A = list(map(int,input().split()))
    print(math.ceil(sum(A)/len(A)))