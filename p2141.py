n = int(raw_input())
s = raw_input().split()
x = []
repeat = 0
for i in range(0, n):
    x.append(int(s[i]))
y = set(x)
z = set()
for i in range(0, n):
    for j in range(i+1, n):
        if y.__contains__(x[i]+x[j]):
            z.add(x[i]+x[j])
print z.__len__()