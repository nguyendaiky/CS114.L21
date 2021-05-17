
def function(k,t):
    if k == t == 0:
        return 0
    elif t == 0:
        return 0
    if (t//k) % 2 == 0:
        return (t%k)
    else:
        return k-(t%k)
kt = input().rstrip().split()
k = int(kt[0])
t = int(kt[1])
ans = function(k,t)
print(ans)
