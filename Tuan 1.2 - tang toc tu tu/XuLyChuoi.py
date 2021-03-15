s = str(input().rstrip().lower())
s = s.replace('a','')
s = s.replace('o','')
s = s.replace('y','')
s = s.replace('e','')
s = s.replace('u','')
s = s.replace('i','')
ans = ""
for i in range(len(s)):
    ans += '.'
    ans += s[i]
print(ans)