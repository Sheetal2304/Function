def max_number():
    a=list(input("enter the number"))
    #a=list(a)
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    print(a[-1])
max_number()






