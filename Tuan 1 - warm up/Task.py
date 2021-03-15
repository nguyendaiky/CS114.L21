def function(n,k,p,q):
    A = p*2+q-2
    B = 0
    if A<1 or A > n:
        print(-1) 
    else:
        if A-k>0:
            B = A-k
        else:
            B = A+k
        if B > n:
            print(-1)
        else:
            if B%2 == 0:
                v = 2
            else:
                v = 1
            u = (B-(v-2))/2
            print(int(u),v)
n = int(input())
k = int(input())
p = int(input())
q = int(input())
function(n,k,p,q)
