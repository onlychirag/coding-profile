from itertools import chain
from operator import mod, xor
from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
from functools import reduce
import bisect
import math
import heapq
input = lambda: stdin.readline().rstrip()
m=10**9+7
def pow(p,o):
    if o==0:
        return 1
    temp=pow(p,o//2)
    temp=temp%m
    temp*=temp
    temp=temp%m
    if o%2:
        return (temp*(p%m))%m
    return temp
def mi(i,m):
    return pow(i,m-2)
def mul(a,b):
    return ((a%m)*(b%m))%m
ss=2*(10**5)+1
f=[0]*ss
fa=[0]*ss
f[0]=fa[0]=1
for i in range(1,ss):
    f[i]=mul(f[i-1],i)
    fa[i]=mul(fa[i-1],mi(i,m))
for _ in range(int(input())):
    
    n=int(input())
    #a,b=(map(int,input().split()))
    c=list(map(int,input()))
    d=list(map(int,input()))
    a=0
    for i,j in zip(c,d):
        if i==j:
            a+=1
    if (n-a)%2:
        print(0)
        continue
    n-=a
    ans=pow(2,a)
    ans=mul(ans,mul(f[n],mul(fa[n//2],fa[n//2])))
    print(ans)