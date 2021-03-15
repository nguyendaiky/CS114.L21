a = int(input())
S = 0
for i in range(1,a):
    if a%i==0:
        S+=i
print(S)