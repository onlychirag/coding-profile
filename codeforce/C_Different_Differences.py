dp=[]
i=0
an=(i*(i+1))//2
while an<=40:
    dp.append(an)
    i+=1
    an=(i*(i+1))//2
#print(dp)
from bisect import bisect_left
import bisect
for i in range(int(input())):
    a,b=map(int,input().split())
    ans=[1]*(a)
    c=bisect.bisect(dp,b-a)
    c=min(c,a)
    l=0
    for i in range(1,a):
        if c:
            ans[i]+=ans[i-1]+l
            l+=1
            c-=1
        else:
            ans[i]+=ans[i-1]
    ans[-1]=b
    m=set()
    for i,j in zip(ans,ans[1:]):
        m.add(j-i)
    print(len(m))