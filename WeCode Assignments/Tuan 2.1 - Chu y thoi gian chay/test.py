
import sys

input = sys.stdin.readline
out = list()

while True:
    iterInput = map(int,input().split())
    control = next(iterInput)
    if control == 0:
        out.insert(0, next(iterInput))
    elif control == 1:
        out.append(next(iterInput))
    elif control == 3:
        break
sys.stdout.write(' '.join(map(str,out)))