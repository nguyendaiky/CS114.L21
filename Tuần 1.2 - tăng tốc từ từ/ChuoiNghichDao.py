s1 = str(input().rstrip())
s2 = str(input().rstrip())
count = 0
if len(s1) == len(s2):
    for i in range(len(s1)):
        if s1[i] != s2[len(s2)-1-i]:
            count += 1
    if count == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
