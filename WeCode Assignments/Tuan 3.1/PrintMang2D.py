r, c = map(int,input().split())
arr = []
for i in range(r):
    t1 = [int(i) for i in input().split()]
    t2 = list(map(str,t1))
    arr.append(t2)

length = []
for j in range(c):
    maxx = 0
    for i in range(r):
        t = len(arr[i][j])
        if t > maxx:
            maxx = t
    length.append(maxx)  

for i in range(r):
    for j in range(c):
        if len(arr[i][j]) != length[j]:
            arr[i][j] = ' '*(length[j]-len(arr[i][j])) + arr[i][j]
        if j != c-1:
            print(arr[i][j], end=' ')
        else:
            print(arr[i][j])