import math
a = int(input())
# A = []
# for i in range(a):
#     m,n = map(int,input().split())
#     A.append([m,n])
for i in range(a):
    m,n = map(int,input().split())
    x = math.gcd(m,n)
    tu = m//x
    mau = n//x
    if mau==1:
        print(tu)
    else:
        print(tu,mau)
