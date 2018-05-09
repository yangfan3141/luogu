cash = 0
saving = 0
month = 0
for i in range(1,13):
    cash = cash + 300 - int(raw_input())
    if cash < 0:
        month = 0-i
        break
    else:
        if cash >= 100:
            saving = saving + int(cash/100)
            cash = cash - 100*int(cash/100)
if month < 0:
    print month
else:
    print saving*120+cash