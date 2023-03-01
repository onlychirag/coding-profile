from sys import stdin
import sys
from collections import Counter
from collections import defaultdict

mod=998244353
    
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    #n=int(input())
    an=0
    c=a
    while c<=b:
        an+=1
        c*=2
    ans=0
    
    #while True:
    m=b//(2**(an-1))-a+1
    n=(b)/(2**(an-2)*3)-a+1
    n=max(int(n),0)
    print(an,(n*(an-1)+m)%mod)