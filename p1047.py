s = raw_input().split()
l = int(s[0])
m = int(s[1])
a = []
for i in range(0,l+1):
    a.append(int(1))
for i in range(0,m):
    x = raw_input().split()
    first = int(x[0])
    last = int(x[1])
    for j in range(first-1,last):
        a[j]=0
for i in range(1,l+1):
    a[0] = a[0] + a[i]
print a[0]
