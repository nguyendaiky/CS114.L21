import array as a
import sys

input = sys.stdin.readline

output = a.array('L')

while True:
    iteInput = map(int, input().split())
    control = next(iteInput)

    if control == 0:
        output.insert(0, next(iteInput))
    elif control == 1:
        output.append(next(iteInput))
    elif control == 2:
        x = next(iteInput)
        y = next(iteInput)
        if x in output:
            output.insert(output.index(x) + 1, y)
        else:
            output.insert(0, y)
    elif control == 3:
        x = next(iteInput)
        if x in output:
            output.remove(x)
    elif control == 4:
        x = next(iteInput)
        while x in output:
            output.remove(x)
    elif control == 5:
        if(len(output) > 0):
            output.remove(output[0])
    else:
        break

if len(output) == 0: print("blank")
else:
    sys.stdout.write(' '.join(map(str, output))+"\n")