n = int(input())
A = list(map(float,input().split()))
kx = input().split()
k = int(kx[0])
x = float(kx[1])
Ans = []
if x <= A[0]:
    for i in range(k):
        Ans.append(int(A[i]))
elif x >= A[-1]:
    for i in range(k):
        Ans.append(int(A[n-1-i]))
while len(Ans)<3:
    for i in range(len(A)):
        min = 10*1000000
        if abs(A[i]-x) < min:
            Ans.append(int(A[i]))
            A.remove(A[i])
            break

Ans = list(map(str,sorted(Ans)))
ans = ' '.join(Ans)
print(ans)