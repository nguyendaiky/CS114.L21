import math
n,m,a = map(int,input().split())
t1 = math.ceil(n/a)
t2 = math.ceil(m/a)
print(t1*t2)
