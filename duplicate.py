def duplicate(list1):
    # list1=
    list2=[]
    i=0
    while i<len(list1):
        count=0
        j=0
        while j<len(list1):
            if list1[j]==list1[i]:
                count+=1
            j+=1
        if list1[i]in list2:
            i+=1
            continue
        list2.append(list1[i])
        print(list1[i],"",count)
        i+=1
    print(list2)
duplicate(["a","b","c","d","c","a","b","e","a","d","b","c","e","f"])