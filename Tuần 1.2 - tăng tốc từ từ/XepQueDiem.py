q = int(input())
for i in range(q):
    n = int(input())
    if n == 2:
        print(2)
        continue
    if n%2==0:
        print(0)
    else:
        count = 0
        while n%2!=0:
            n += 1
            count += 1
        print(count)