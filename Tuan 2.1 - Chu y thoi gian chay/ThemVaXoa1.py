import sys 
input = sys.stdin.readline
list = []
while True:
    arr = input().split()
    option = int(arr[0])
    if len(arr) == 2:
        value = int(arr[1])
        if option == 0:
            list.insert(0,value) 
        elif option == 1:
            list.append(value)
        elif option == 3:
            try:
                list.remove(value)
            except ValueError:
                continue
        else:
            for i in range(list.count(value)):
                list.remove(value)

    elif len(arr) == 3:
        value1, value2 = int(arr[1]), int(arr[2])
        try:
            list.insert(list.index(value1) + 1, value2)
        except ValueError:
            list.insert(0, value2)

    elif len(arr) == 1:
        if option == 5:
            try:
                list.pop(0)
            except ValueError:
                continue
        else:
            break

if len(list) == 0:
    print('blank')
else:
    sys.stdout.write(' '.join(map(str, list))+"\n")