from itertools import chain
from operator import xor
from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
from functools import reduce
import bisect
import math
import heapq
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    def s(n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
    n=(input())
    l=""
    r=""
    a=0
    for i in range(len(n)):
        if int(n[i])%2:
            if a%2:
                l+=str(int(n[i])//2)
                r+=str(int(n[i])//2+1)
                a+=1
            else:
                l+=str(int(n[i])//2+1)
                r+=str(int(n[i])//2)
                a+=1
        else:
            l+=str(int(n[i])//2)
            r+=str(int(n[i])//2)
    print(int(l),int(r))
    continue
    f=0
    if set(str(n))==set("9"):
        f=1
    l=len(str(n//2))-f
    if abs(s(n//2)-s(n//2+n%2))>1:
        print(n//2-int("4"*l),n//2+int("4"*l)+n%2)
        
    else:

        print(n//2,n//2+n%2)