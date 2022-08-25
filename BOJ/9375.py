import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    closet = dict()
    n = int(input())
    for _ in range(n):
        x, cloth = map(str, input().split())
        if cloth in closet:
            closet[cloth] += 1
        else:
            closet[cloth] = 1
    if len(closet) == 1:
        result.append(sum(closet.values()))
    else:
        mul = 1
        for val in closet.values():
            mul *= val
        result.append(sum(closet.values())+mul)

for x in result:
    print(x)