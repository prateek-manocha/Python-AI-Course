def binary_search_recurse(mylist,value):
    if value> mylist[-1] or value<mylist[0]:
        result = 'Not in list'
        return result
    middle = len(mylist)//2
    if mylist[middle] == value:
        return 'Found the element'
    elif value>mylist[middle]:
        return binary_search_recurse(mylist[middle+1:],value)
    else:
        return binary_search_recurse(mylist[:middle],value)

mylist = [0,1,3,5,6,7,8,9,11]
value = int(input('Enter the value: '))
result = binary_search_recurse(mylist,value)
print(result)

def binary_search_loop(mylist,value):
    if value> mylist[-1] or value<mylist[0]:
        result = 'Not in list'
        return result

    while len(mylist)>0:
        mid = len(mylist)//2
        if mylist[mid] == value:
            return 'Found'
        elif value> mylist[mid]:
            mylist = mylist[mid+1:]
        else:
            mylist = mylist[:mid]
    return 'Not found.'

result = binary_search_loop(mylist, value)
print(result)
