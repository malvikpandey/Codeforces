limak, bb = map(int, input().split())
count = 1

while limak <= bb :
    limak = limak*3
    bb = bb*2
    if limak <= bb:
        count += 1


print(count)