def title():
    a=list(input("enter the number"))
    #a=list(a)
    # a=[5,7,3,2,9,1,4]
    i=0
    while i<len(a):
        j=0
        while j<len(a)-1:
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            j+=1
        i+=1
    print(a)
title()


# def title():
#     a=list(input("enter the number"))
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(a)-1:
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#             j+=1
#         i+=1
#     return(a)
# print(title(a))




