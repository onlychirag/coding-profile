from cmath import log
from sys import stdin
import sys
from collections import Counter
import math
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    def f(x):
        if x==1:
            return 0
        if x%2==0:
            return 1+f(x//2)
        if x%2:
            return f(x//2)
    def g(x):
        if x==1:
            return 1
        if x%2==0:
            return 1+2*(g(x//2))
        if x%2:
            return 2*(g(x//2))
    a,b=map(int,input().split())
    ans=0

    p=math.log2(b)
    t=pow(2,int(p))
    t=int(t)
    if t>=a:
        print(f(t)+g(t))
        continue
    for i in range(a,min(a+50,b+1)):
        ans=max(ans,f(i)+g(i))
    print(ans)