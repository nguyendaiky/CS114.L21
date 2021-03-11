a = str(input().rstrip())
S = 0
for i in a:
    S += int(i)**(len(a))
if S == int(a):
    print('True')
else: 
    print('False')