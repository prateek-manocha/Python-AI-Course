def select_sort(mylist):

    for i in range(len(mylist)-1):
        midx = i
        for j in range(i+1,len(mylist)):
            if mylist[j]<mylist[midx]:
                midx = j
        mylist[i], mylist[midx] = mylist[midx], mylist[i]
        print(mylist)

mylist = [1,4,6,3,2]
select_sort(mylist)
print('Final output: ', end='  ')
print(mylist)
