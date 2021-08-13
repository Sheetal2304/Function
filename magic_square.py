def magic_square(a):
    # a=[[8,3,4],
    #    [1,5,9],
    #    [6,7,2]]
    magic_sum =15
    row_list=[]
    col_list=[]
    i=0
    while i<len(a):
        row=0
        col_sum=0
        row_sum=0
        while row<len(a[i]):
            row_sum=row_sum+a[i][row]
            col_sum=col_sum+a[row][i]
            row+=1
        i+=1
        row_list.append(row_sum)
        col_list.append(col_sum)
    #print(row_list)
    #print(col_list)
    x=0
    y=len(a)-1
    d=0
    dia_1=0
    dia_2=0
    while d<len(a):
        dia_1=dia_1+(a[d][x])
        dia_2=dia_2+(a[d][y])
        y-=1
        x+=1
        d+=1
    #print(dia_2,dia_1)
    if row_list==col_list:
        if dia_1==dia_2==magic_sum:
            print("it is a magic square")
        else:
            print("it is not a magic square")
magic_square([[8,3,4],
              [1,5,9],
              [6,7,2]])