a,b = map(int,input().split())
A = list(map(int,input().rstrip().split()))
B = list(map(int,input().rstrip().split()))
Merge = [None]*(a+b)
i = j = k = 0
while i < a and j < b:
    if A[i] < B[j]:
        Merge[k] = A[i]
        k += 1
        i += 1
    else:
        Merge[k] = B[j]
        k += 1
        j += 1
while i < a:
    Merge[k] = A[i]
    k += 1
    i += 1
while j < b:
    Merge[k] = B[j]
    k += 1
    j += 1
result = ' '.join(map(str,Merge))
print(result)