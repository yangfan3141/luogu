n = raw_input().split()
h = int(raw_input()) + 30
x = 0
for i in range(0,len(n)):
    if h >= int(n[i]):
        x = x + 1
print x