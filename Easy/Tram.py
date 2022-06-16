number = input()
flag = 'N'
for i in number:
    if i == "7" or i == "4":
        flag = 'Y'
    if flag == 'Y':
        continue
    elif flag == 'N':
        break

if flag == 'Y':
    print("YES")
else :
    print("NO")