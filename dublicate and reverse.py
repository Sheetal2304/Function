# list1=[1,1,1,1,3,4,6,8,8,0,3,2,0,1,10]
# list2=[]
# i=0
# while i<len(list1):
#     if list1[i]in list2:
#         i+=1
#         continue
#     list2.append(list1[i])
# print(list2)
# b=[]
# i=1
# while i<len(list2)+1:
#     b.append(list2[-i])
#     i+=1
# print(b) 

def reverse(list1):
    list2=[]
    i=0
    while i<len(list1):
        if list1[i]in list2:
            i+=1
            continue
        list2.append(list1[i])
    print(list2)
    b=[]
    i=1
    while i<len(list2)+1:
        b.append(list2[-i])
        i+=1
    print(b) 
reverse ([1,1,1,1,3,4,6,8,8,0,3,2,0,1,10])
