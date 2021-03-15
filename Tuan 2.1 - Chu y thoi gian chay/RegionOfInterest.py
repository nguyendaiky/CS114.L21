h,w = map(int,input().split())
array = []
ans = []
for _ in range(h+1):
    array.append(list(map(int,input().split())))
    ans.append([0]*w)
top,left,bottom,right = map(int,input().split())

for i in range(top,bottom+1):
    for j in range(left,right+1):
        ans[i][j] = array[i][j]
for r in ans:
    for c in r:
        print(c, end=' ')
    print()