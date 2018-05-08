s = raw_input().split()
x = int(s[2])-int(s[0])
y = int(s[3])-int(s[1])
if y < 0:
    x = x - 1
    y = y + 60
print x, y