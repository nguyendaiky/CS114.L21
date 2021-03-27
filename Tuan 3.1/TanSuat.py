q = int(input())
for i in range(q):
    n,k = map(int,input().split())
    arr = [int(i) for i in input().split()]
    count = 0
    for i in arr:
        if i == k:
            count += 1
    print(count)