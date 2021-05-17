dict = {}
while True:
    array = [int(i) for i in input().split()]
    if array[0] == 0:
        break
    elif array[0] == 1:
        dict[array[1]] = 1
    elif array[0] == 2:
        if array[1] in dict:
            print(dict[array[1]])
        else:
            print(0)
    

