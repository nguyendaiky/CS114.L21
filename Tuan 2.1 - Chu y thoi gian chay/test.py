n = int(input())
array = list(map(int,input().split()))
k, a = map(int,input().split())
result = []

for i in range(0,k):
    number = min(array,key=lambda x: abs(a-x))
    array.remove(number)
    result.append(number)
print(result)