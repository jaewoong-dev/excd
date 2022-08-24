from math import factorial
import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    result.append(factorial(M)//(factorial(N)*factorial(M-N)))

for x in result:
    print(x)