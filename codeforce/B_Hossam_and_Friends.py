from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    #a=int(input())
    a,b=(map(int,input().split()))
    dp=[1]*(a+1)
    for i in range(b):
        c,d=(map(int,input().split()))
        if c>d:
            dp[c]=max(dp[c],d+1)
        else:
            dp[d]=max(dp[d],c+1)
    ans=0
    for i in range(1,a+1):
        dp[i]=max(dp[i],dp[i-1])
        ans+=i-dp[i]+1
    print(ans)