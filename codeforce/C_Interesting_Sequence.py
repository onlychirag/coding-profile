from operator import xor
from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
from functools import reduce

import heapq
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a,b=map(int,input().split())
    d=""
    flag=0
    if len(str(bin(a)))!=len(str(bin(b))) and b!=0:
        print(-1)
        continue
    for i,j in zip(str(bin(a)[2:]),str(bin(b)[2:])):
        if i=="0" and j=="1":
            flag=1
            break
        
    #print(d)
    l=bin(a)[2:]
    p=bin(b)[2:]
    pp=len(l)
    o="1"+"0"*(pp-1)
    k=l[:2]
    if k!="10" and p!=o and b!=0:
        print(-1)
        continue
    for i in str(bin(a)[2:]):
        if i=="0":
            d+="1"
        else:
            d+="0"
    p=int(d,2)
    if flag:
        print(-1)
        continue
    if b==0:
        print(a+p+1)
    else:
        print(a+a-b)