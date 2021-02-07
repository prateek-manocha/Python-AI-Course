def bubble_sort(mylist):
    for i in range(len(mylist)-1):
        for j in range(len(mylist)-1-i):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
        print(mylist)

mylist = [1,4,6,3,2,0,0,1,9,8,100]
bubble_sort(mylist)
print('Final output: ', end='  ')
print(mylist)
