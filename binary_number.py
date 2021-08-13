def title(a):
    b=[]
    i=1
    while i<len(a)+1:
        b.append(a[-i])
        i+=1
    #print(b)
    sum=0
    j=0
    while j<len(b):
        if b[j]==1:
            sum=sum+(2**j)
        j+=1
    print(sum)
title([1,0,1,1])