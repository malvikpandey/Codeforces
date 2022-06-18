n, k = map(int, input().split())

if n % 2 == 0:
        c = n / 2
else:
        c = (n + 1) / 2

if k <= c:
    print(int((k * 2) - 1))
else:
    print(int((k - c) * 2))