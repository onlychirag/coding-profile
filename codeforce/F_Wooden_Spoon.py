from operator import mod
from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
mod=998244353
#for _ in range(int(input())):
n=int(input())
#a,b=(map(int,input().split()))
#c=list(map(str,input()))
#d=list(map(str,input()))
e=2**n
d=[0]*21
d[n]=1
dd=[0]*21
ddd=[0]*(e+1)
dp=[[0]*e for i in range(21)]
for i in range(n):
    d[i]=2**(n-i-1)
dd[0]=d[0]
dp[0][0]=dd[0]
for i in range(1,n+1):
    dd[i]=dd[i-1]+d[i]
for i in range(1,e+1):
    ddd[i]=ddd[i-1]*i%mod
for i in range(1,n+1):
    for j in range(1,e):
        dp[i][j]=(dp[i-1][j-1]*d[i]%mod + dp[i][j-1]*(dd[i-1]-j+1))%mod
for i in range(e):
    print((dp[n][i]*ddd[e-i-1]*e)%mod)    