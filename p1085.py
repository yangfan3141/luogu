x = 7
y = 8
for i in range(0, 7):
    s = raw_input().split()
    z = int(s[0])+int(s[1])
    if(z>x):
        x = z
        y = i
if y == 8:
    y = -1
print y+1
