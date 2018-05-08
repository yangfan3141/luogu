for i in range(102,330):
    x = i*2
    y = i*3
    i1 = int(i/100)
    i2 = int((i-i1*100)/10)
    x1 = int(x/100)
    x2 = int((x-x1*100)/10)
    y1 = int(y/100)
    y2 = int((y-y1*100)/10)
    z = {i%10,x%10,y%10,i1,i2,x1,x2,y1,y2,0}
    if (z.__len__() == 10):
        print i,i*2,i*3