from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    if a==3:
        print("NO")
        continue

    print("YES")
    if a%2!=1:
        for i in range(1,a+1):
            if i%2:
                print(1,end=" ")
            else:
                print(-1,end=" ")
        print()
        continue
    l=a//2
    for i in range(a):
        if i%2:
            print(-l,end=" ")
        else:
            print(l-1,end=" ")
    print()        