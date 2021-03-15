q = int(input())
for i in range(q):
    s = str(input())
    t = str(input())
    count = 0
    for i in s:
        if i in t:
            count+=1
    if count > 0:
        print('YES')
    else:
        print('NO')

