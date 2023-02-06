from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(str,input()))
    e=Counter(c)
    f=Counter(c)
    ans=len(set(c))
    p=ans
    q=0
    for i in range(a):
        if e[c[i]]==f[c[i]]:
            q+=1
        e[c[i]]-=1
        if e[c[i]]==0:
            p-=1
        ans=max(ans,p+q)
    print(ans)