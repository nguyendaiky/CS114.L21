h, w = map(int,input().split())
array = ''
for i in range(h):
    row = input()[0:(w*2-1)]
    array += row + ' '
top, left, bottom, right = [int(x) for x in input().split()]

zeroRow = '0'
for i in range(w-1):
    zeroRow += ' 0'
for r in range(h):
    if r < top or r > bottom or top > bottom or left > right:
        print(zeroRow)
    else:
        print(zeroRow[0:(left*2)], end='')

        begin = r*w*2 + left*2
        end = begin + (right-left)*2+2
        roi = array[begin:end].split()
        for i in roi:
            print(i, end= ' ')

        print(zeroRow[(right*2+2):(w*2-1)])


