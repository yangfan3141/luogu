s = raw_input().split()
x = int(s[0])
n = int(s[1])
d = 0
for i in range(0,int(n%7)):
    if x + i < 6:
        d = d + 250
    else:
        if x + i > 7:
            d = d + 250
print d + 1250*int(n/7)