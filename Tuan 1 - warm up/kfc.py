def FtoC(val):
    return ((5/9)*(val-32))
def FtoK(val):
    return (5/9*(val-32)+273.15)
val = float(input())
print("{:g} {:g}".format(FtoC(val),FtoK(val)))
# c = round(FtoC(val),3)
# k = round(FtoK(val),3)
# if int(c) == c:
#     c = int(c)
# if int(k) == k:
#     k = int(k)
# print("{C} {K}".format(C=c,K=k))

