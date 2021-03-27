import bisect 
n=int(input())
lst=[int(i) for i in input().split()]

def function(lst,valList):
    k,x=[int(i) for i in valList.split()]
    pivot=bisect.bisect_left(lst, x)
    
    if pivot==len(lst):
        print(lst[len(lst)-k],' ',lst[len(lst)-1])
    elif pivot==0:
        print(lst[0],' ',lst[k-1])
    else:
        ans=[]
        l=pivot
        r=pivot+1
        if lst[pivot]==x or x-lst[l] <= lst[r]-x:
            ans.append(lst[pivot])
            l-=1
        else:
            ans.append(lst[pivot+1])
            r+=1
        while len(ans)!=k:   
            if l<0 and r<len(lst)-1:
                ans.append(lst[r])
                r+=1
            elif l>=0 and r >len(lst)-1:
                ans.append(lst[l])
                l-=1
            else:
                if x-lst[l]<=lst[r]-x:
                    ans.append(lst[l])
                    l-=1
                else:
                    ans.append(lst[r])
                    r+=1
        ans.sort()
        print(ans[0],' ',ans[len(ans)-1])
while True:
    valList=input()
    if valList=='':
        break
    else:
        function(lst,valList)