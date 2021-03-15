array1 = []
a = -1
while a != 0:
    ab = list(map(int,input().split()))
    try:
        a = ab[0]
        b = ab[1]
    except:
        a = ab[0]
    if a == 1:
        array1.append(b)
    elif a == 2:
        if b in array1:
            print(1)
        else:
            print(0)

