s = str(input())
count = 0
for i in s:
    if i == '4' or i == '7':
        count += 1
c = str(count)
count = 0
for i in c:
    if i != '4' and i != '7':
        count += 1
if count == 0:
    print('YES')
else:
    print('NO')