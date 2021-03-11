h,w = map(int,input().split())
array = []
for _ in range(h):
    array.append(list(map(int,input().split())))
top,left,bottom,right = map(int,input().split())
print(array)
for i in range(h):
    for j in range(w):
        if i >= top and i <= bottom: #and j >= left and j <= right:
            print(array[i][j],end=' ')
        # if i < a and i >= c and j < b and j >= d:
        #     array[i][j] = 0
# print(array)