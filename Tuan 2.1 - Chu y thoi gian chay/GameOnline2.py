import sys
input = sys.stdin.readline
dict = {}
ans = []
while True:
    arr = input().split()
    if len(arr)>0:
        if arr[0] == '0':
            break
        elif arr[0] == '1':
            dict[arr[1]] = True 
        elif arr[0] == '2':
            if arr[1] in dict and dict[arr[1]] == True:
                ans.append(1)
            else:
                ans.append(0)
        elif arr[0] == '3' and arr[1] in dict:
                dict[arr[1]] = False 
for i in ans:
    print(i)