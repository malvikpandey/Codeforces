number = input()
lucky = 0

for i in number:
    if i == "7" or i == "4":
        lucky += 1
    else:
        continue

if lucky == 7 or lucky == 4:
    print("YES")
else :
    print("NO")