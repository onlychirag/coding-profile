a=list(map(int,input().split()))
pre=[0]*5
ans=sum(a)
pre=0
aa=0
for i in a:
    print(pre+i)
    if pre+i<ans:
        pre=pre-i
        aa+=1
        ans-=2*i
    else:
        pre+=i
print(aa)