s = raw_input()
n = int(s[0])
s = raw_input().split()
a = []
b = []
for i in range(0,n):
    a.append(int(s[i]))
    b.append(int(0))
for i in range(0,n):
    for j in range(0,i):
        if a[j]<a[i]:
            b[i] = b[i] + 1
for i in range(0,n-1):
    print(b[i]),
print b[n-1]