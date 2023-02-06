from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
mod=998244353
for _ in range(int(input())):
    a=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(str,input()))
    dp=[0]*a
    dp1=[0]*a
    dp[0],dp1[0]=1,1
    for i in range(1,a):
        if c[i-1]!=c[i]:
            dp[i]=dp1[i]=dp1[i-1]
        else:
            dp[i]=dp[i-1]*2
            dp[i]%=mod
            dp1[i]=dp1[i-1]
    ans=0
    for i in dp:
        ans+=i
        ans%=mod
    print(ans)