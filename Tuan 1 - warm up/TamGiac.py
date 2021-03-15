import math
a = int(input())
b = int(input())
c = int(input())
if not((a+b>c) and (a+c>b) and (b+c>a)):
    print("Khong phai tam giac")
else:
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if S == int(S):
        S = int(S)
    else:
        S = round(S,2)
    if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (b**2+c**2==a**2):
        print("Tam giac vuong"+", dien tich = {s}".format(s=S))
    elif a == b == c:
        print("Tam giac deu"+", dien tich = {s}".format(s=S))
    elif (a==b) or (a==c) or (b==c):
        print("Tam giac can"+", dien tich = {s}".format(s=S))
    else: 
        print("Tam giac thuong"+", dien tich = {s}".format(s=S))
    
