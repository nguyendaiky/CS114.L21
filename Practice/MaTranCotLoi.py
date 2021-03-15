A = []
for i in range(5):
    A.append(list(map(int,input().rstrip().split())))
markX = -1
markY = -1
for i in range(5):
    for j in range(5):
        if A[i][j] == 1:
            markX = i
            markY = j
print(abs(markX-2)+abs(markY-2))