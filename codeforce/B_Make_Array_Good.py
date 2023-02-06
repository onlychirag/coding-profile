from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(int,input().split()))
    ans=[]
    d=[]
    m=min(c)
    for i,j in enumerate(c):
        d.append([j,i])
    d.sort()
    for i in range(1,len(d)):
        l=d[i][0]
        p=d[i-1][0]
        if l%p!=0:
            ans.append([d[i][1]+1,p-l%p])
            d[i][0]+=p-l%p
    print(len(ans))
    for i,j in ans:
        print(i,j)