s = int(raw_input())
if s <= 150:
    print round(s*0.4463,1)
else:
    if s <= 400:
        print round(150*0.4463 + (s-150)*0.4663,1)
    else:
        if s > 400:
            print round(150*0.4463 + 250*0.4663 + (s-400)*0.5663,1)