'''12. Write a function list_overlap(list1,list2) that takes two lists of integers as input, and returns a
list of the common elements. Don't use sets for this.
'''
list1 = list(range(10,25))
list2 = list(range(0,15,2))

common = list(set(list1)&set(list2))
print('Common elements using sets: '+str(common))

def common_values_nested(list1, list2):
    common_list = []
    for i in list1:
        for j in list2:
            if i == j:
                common_list.append(i)
    return common_list

def common_values_in(list1, list2):
    common_list = []
    for i in list1:
        if i in list2:
            common_list.append(i)
    return common_list

print('Common elements using nested for loop: '+str(common_values_nested(list1, list2)))
print('Common elements using for loop and in: '+str(common_values_in(list1, list2)))

common_list_elements = [common for common in list1 if common in list2]
print('Common elements using nested for loop in short: '+str(common_list_elements))











#end
