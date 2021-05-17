import sys
m, n = map(int, input().split())
r, c = map(int, input().split())

array = []
if m * n != r * c:
    r = m
    c = n

for i in range(0, m):
    array += sys.stdin.readline().split()
    while len(array) >= c:
        sys.stdout.write(' '.join(array[0:c])+'\n')
        array = array[c:]