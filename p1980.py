s = raw_input().split()
n = int(s[0])
x = int(s[1])
t = 0
for i in range(1,n+1):
    temp = str(i)
    y = str(x)
    t = t + int(temp.count(y))
print t