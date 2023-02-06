from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
mod=998244353
#for _ in range(int(input())):
a,b=map(int,input().split())
d=[0]*(a+1)
dp=[0]*(a+1)
o=pow(2,mod-2,mod)
dp[1]=o
d[1]=o
an=0
for i in range(2,a+1):
    c=pow(b,i,mod)
    c=pow(c,mod-2,mod)
    an=d[i-1]+(pow(c,2,mod)*o)%mod+(c*dp[i-1])%mod
    an=an%mod
    d[i]=an
    dp[i]=(dp[i-1]+(c*o)%mod)%mod
for i in range(1,a+1):
    print(d[i],end=" ")
print()
    