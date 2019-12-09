n = int(raw_input())
s = raw_input().split()
temp = 1
maxlen = 1
for i in range(1, n):
    if int(s[i]) > int(s[i-1]):
        temp = temp + 1
    else:
        if temp > maxlen:
            maxlen = temp
        temp = 1
if maxlen > temp:
    print maxlen
else:
    print temp
