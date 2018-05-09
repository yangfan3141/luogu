s = float(raw_input())
i = 1
d = 2
t = 2
while t < s:
    d = d * 0.98
    t = t + d
    i = i + 1
print i