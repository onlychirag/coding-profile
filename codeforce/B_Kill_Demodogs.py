from sys import stdin
import sys
from collections import Counter
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    a=int(input())
    b=input()
    def lo(s: str) -> int:
        n = len(s)
        dp, dpPrev = [0] * n, [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[j] = dpPrev[j - 1] + 2
                else:
                    dp[j] = max(dpPrev[j], dp[j - 1])
            dp, dpPrev = dpPrev, dp

        return dpPrev[n - 1]
    print(lo(b)//2)