x = int(input())
y = int(input())
z = int(input())
maximum = [x+y*z, x*(y+z), x*y*z, (x+y)*z, x+(y*z), (x*y)+z, x*y+z, x+y+z]

print(max(maximum))