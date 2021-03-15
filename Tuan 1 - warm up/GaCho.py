def calc(xxx,yy):
    t = (yy-2*xxx)/2
    return (xxx - t,t)
xxx, yy = map(int,input().rstrip().split())
Ga, Cho = map(int,calc(xxx,yy))
print(Ga,Cho)
