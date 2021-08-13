def palindrome():
    a=list(input("enter the name  "))
    #a=list(a)
    b=[]
    i=1
    while i<len(a)+1:
        b.append(a[-i])
        i+=1
    #print(b)
    if a==b:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
palindrome()