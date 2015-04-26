def zheban(list,x):
    start=0
    if list[0]==x:
        return 0
    end=len(list)-1
    while(start==end):
        if(x==list[start]):
            return start
        else:
            return error
    if(start<end):
        middle=start+(end-start)//2
        if list[middle]<x:
            start=middle+1
        elif list[middle]>x:
            end=middle-1
        else:
            return middle
