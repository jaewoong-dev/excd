N, K = map(int, input().split())

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(N)//(factorial(K)*factorial(N-K)))