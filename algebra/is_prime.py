def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True
from bisect import bisect_left
from sys import stdin
import sys
from collections import Counter, defaultdict
input = lambda: stdin.readline().rstrip()

for _ in range(int(input())):
    a,b=map(int,input().split())
    #n=int(input())
#    bb=list(map(int,input().split()))
    s=set()
    for i in range(a,b+1):
        for j in range(a,b+1):
            if i+j==i^j:
                s.add(i+j)
    print(len(s))