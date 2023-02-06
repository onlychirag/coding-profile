import enum
from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input()))
    dp=[0]*a
    for i in range(1,a):
        if c[i]!=c[i-1]:
            dp[i]=dp[i-1]+1
        else:
            dp[i]=dp[i-1]
    ans=float("inf")
    for i in reversed(range(a)):
        if i-b+1<0:
            break
        l=dp[i]-dp[i-b+1]
        if c[i]==0:
            l+=1
        ans=min(ans,l)
    print(ans)