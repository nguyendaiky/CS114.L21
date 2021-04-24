import time
start_time = time.time()

Colors = input().strip().split()
Steps = input().strip().split()
Dot = input()
Steps.reverse()
rubik = [] 
for color in Colors:
    temp = []
    for i in range(9):
        temp.append(color)
    rubik.append(temp)

formula = {
    "U":[0, 3, 2],
    "U'":[0, 3, 2],
    "u":[0, 3, 2],
    "u'":[0, 3, 2],

    "B":[1, 2, 3],
    "B'":[1, 2, 3],
    "b":[1, 2, 3],
    "b'":[1, 2, 3],

    "L":[2, 1, 0],
    "L'":[2, 1, 0],
    "l":[2, 1, 0],
    "l'":[2, 1, 0],
    
    "R":[3, 0, 1],
    "R'":[3, 0, 1],
    "r":[3, 0, 1],
    "r'":[3, 0, 1],
}
formula2 = [[0, 8, 4], [1, 3, 6], [2, 7, 5], [3, 6, 1]]
One = ["U", "B", "L", "R", "U'", "B'", "L'", "R'"]

for step in Steps:
    for i in range(4):
        if "'" in step:
            temp =rubik[formula[step][2]][formula2[i][2]]
            rubik[formula[step][2]][formula2[i][2]] = rubik[formula[step][1]][formula2[i][1]]
            rubik[formula[step][1]][formula2[i][1]] = rubik[formula[step][0]][formula2[i][0]]
            rubik[formula[step][0]][formula2[i][0]] = temp
        else:
            temp =rubik[formula[step][1]][formula2[i][1]]
            rubik[formula[step][1]][formula2[i][1]] = rubik[formula[step][2]][formula2[i][2]]
            rubik[formula[step][2]][formula2[i][2]] = rubik[formula[step][0]][formula2[i][0]]
            rubik[formula[step][0]][formula2[i][0]] = temp
        if step in One:
            break


for i in range(4):
    print(' '.join(rubik[i]))


print("--- %s seconds ---" % (time.time() - start_time))