n, m = input().split()
m = int(m)
t = 10 ** len(n)
ans = m // t
if m % t >= int(n):
    ans += 1
print(ans)