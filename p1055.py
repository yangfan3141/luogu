sn = raw_input()
check = 0
j = 1
for i in range (0, 11):
    if sn[i] == '-':
        continue
    check = check + int(sn[i])*j
    j = j + 1
check = check % 11
if sn[12] == 'X':
    if check == 10:
        print 'Right'
    else:
        print sn[0:12] + str(check)
else:
    if check == int(sn[12]):
        print 'Right'
    else:
        if check == 10:
            print sn[0:12]+'X'
        else:
            print sn[0:12]+str(check)