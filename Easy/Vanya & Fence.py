n, h = map(int, input().split())
w = 0
a = (input().split())

for i in a:
    if int(i) <= h:
        w += 1
    else:
        w += 2

print(w)

