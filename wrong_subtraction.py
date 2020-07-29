n, k = map(int, input().split())

for x in range(0, k):
    if(n % 10 != 0):
        n -= 1
    else:
        n //= 10

print(n)