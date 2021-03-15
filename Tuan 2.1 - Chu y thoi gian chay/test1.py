h,w = [int(x) for x in input().split()]

zeroLine = '0'
for i in range(w-1):
    zeroLine = zeroLine + ' 0'

image = ''
for i in range(h):
    image = image + input()[0:w*2-1] + ' '

print(image)
