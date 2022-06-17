n, k = map(int, input().split())


for i in range(k):
    p = str(n)
    if p[len(p)-1] == '0' :
        n = int(n/10)
    else:
        n = int(n-1)

print(n)