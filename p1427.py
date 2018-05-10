s = raw_input().split()
a = []
for i in range(0,len(s)):
    if int(s[i]) == 0:
        break
    a.append(s[i])
for i in range(len(a),1,-1):
    print(a[i-1]),
print a[0]