def linearsearch(array,element):
    i=0
    while i<len(array):
        if array[i]==element:
            return i
        i=i+1
    return -1
arr=[4,5,2,8,3,7]
key=8
pos=linearsearch(arr,key)
if pos==-1:
    print("not present")
else:
    print("the element is at",pos)