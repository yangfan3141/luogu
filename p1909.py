pencils = int(raw_input())
s = raw_input().split()
n1 = int(s[0])
p1 = int(s[1])
s = raw_input().split()
n2 = int(s[0])
p2 = int(s[1])
s = raw_input().split()
n3 = int(s[0])
p3 = int(s[1])
if pencils%n1 == 0:
    t1 = int(pencils/n1) * p1
else:
    t1 = int(pencils/n1 + 1) * p1

if pencils%n2 == 0:
    t2 = int(pencils/n2) * p2
else:
    t2 = int(pencils/n2 + 1) * p2

if pencils%n3 == 0:
    t3 = int(pencils/n3) * p3
else:
    t3 = int(pencils/n3 + 1) * p3

print min(t1,t2,t3)