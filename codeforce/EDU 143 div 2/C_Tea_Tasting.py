from sys import stdin
import sys
from collections import Counter,defaultdict
from bisect import bisect_left,bisect_right,bisect
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    pre=[0]*(n+1)
    for i in reversed(range(n)):
        pre[i]=pre[i+1]+d[i]
    su=[0]*(n+1)
    for i in range(n):
        su[i+1]=su[i]+d[i]
        #print(pre)
    for i in range(n):
        pre[i]=max(0,c[i]-pre[i])
    #print(su)
    #print(pre)
    ans=[0]*(n+1)
    for i in range(n):
        if pre[i]==0:
            lk=bisect(su,c[i])
            ans[lk-1]=-su[lk-1]+c[i]    
            print(ans)