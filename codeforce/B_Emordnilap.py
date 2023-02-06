from itertools import chain
from math import factorial
from operator import xor
from sys import stdin
import sys
from collections import Counter
from collections import defaultdict
from functools import reduce
import bisect
import heapq
mod=10**9+7
class Factorial:
    def __init__(self, MOD):
        self.MOD = MOD
        self.factorials = [1, 1]
        self.invModulos = [0, 1]
        self.invFactorial_ = [1, 1]
 
    def calc(self, n):
        if n <= -1:
            print("Invalid argument to calculate n!")
            print("n must be non-negative value. But the argument was " + str(n))
            exit()
        if n < len(self.factorials):
            return self.factorials[n]
        nextArr = [0] * (n + 1 - len(self.factorials))
        initialI = len(self.factorials)
        prev = self.factorials[-1]
        m = self.MOD
        for i in range(initialI, n + 1):
            prev = nextArr[i - initialI] = prev * i % m
        self.factorials += nextArr
        return self.factorials[n]
 
    def inv(self, n):
        if n <= -1:
            print("Invalid argument to calculate n^(-1)")
            print("n must be non-negative value. But the argument was " + str(n))
            exit()
        p = self.MOD
        pi = n % p
        if pi < len(self.invModulos):
            return self.invModulos[pi]
        nextArr = [0] * (n + 1 - len(self.invModulos))
        initialI = len(self.invModulos)
        for i in range(initialI, min(p, n + 1)):
            next = -self.invModulos[p % i] * (p // i) % p
            self.invModulos.append(next)
        return self.invModulos[pi]
 
    def invFactorial(self, n):
        if n <= -1:
            print("Invalid argument to calculate (n^(-1))!")
            print("n must be non-negative value. But the argument was " + str(n))
            exit()
        if n < len(self.invFactorial_):
            return self.invFactorial_[n]
        self.inv(n)  # To make sure already calculated n^-1
        nextArr = [0] * (n + 1 - len(self.invFactorial_))
        initialI = len(self.invFactorial_)
        prev = self.invFactorial_[-1]
        p = self.MOD
        for i in range(initialI, n + 1):
            prev = nextArr[i - initialI] = (prev * self.invModulos[i % p]) % p
        self.invFactorial_ += nextArr
        return self.invFactorial_[n]
 
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    class Factorial:
        def __init__(self, MOD):
            self.MOD = MOD
            self.factorials = [1, 1]
            self.invModulos = [0, 1]
            self.invFactorial_ = [1, 1]
    
        def calc(self, n):
            if n <= -1:
                print("Invalid argument to calculate n!")
                print("n must be non-negative value. But the argument was " + str(n))
                exit()
            if n < len(self.factorials):
                return self.factorials[n]
            nextArr = [0] * (n + 1 - len(self.factorials))
            initialI = len(self.factorials)
            prev = self.factorials[-1]
            m = self.MOD
            for i in range(initialI, n + 1):
                prev = nextArr[i - initialI] = prev * i % m
            self.factorials += nextArr
            return self.factorials[n]
    
        def inv(self, n):
            if n <= -1:
                print("Invalid argument to calculate n^(-1)")
                print("n must be non-negative value. But the argument was " + str(n))
                exit()
            p = self.MOD
            pi = n % p
            if pi < len(self.invModulos):
                return self.invModulos[pi]
            nextArr = [0] * (n + 1 - len(self.invModulos))
            initialI = len(self.invModulos)
            for i in range(initialI, min(p, n + 1)):
                next = -self.invModulos[p % i] * (p // i) % p
                self.invModulos.append(next)
            return self.invModulos[pi]
    
        def invFactorial(self, n):
            if n <= -1:
                print("Invalid argument to calculate (n^(-1))!")
                print("n must be non-negative value. But the argument was " + str(n))
                exit()
            if n < len(self.invFactorial_):
                return self.invFactorial_[n]
            self.inv(n)  # To make sure already calculated n^-1
            nextArr = [0] * (n + 1 - len(self.invFactorial_))
            initialI = len(self.invFactorial_)
            prev = self.invFactorial_[-1]
            p = self.MOD
            for i in range(initialI, n + 1):
                prev = nextArr[i - initialI] = (prev * self.invModulos[i % p]) % p
            self.invFactorial_ += nextArr
            return self.invFactorial_[n]
    
    n=int(input())
    print(((n)*(n-1)*factorial(n))%mod)