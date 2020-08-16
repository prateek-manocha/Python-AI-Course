import numpy as np
list1 = input('Enter the input: ')
final_list = [int(i) for i in list1.split(',')]

def print_box_modified(list):
    matrix = np.zeros((list[0], list[1]), dtype=np.bool)
    print(matrix)
    entry = True
    while entry == True:
        special_box = input('Enter the special box: ')
        print(special_box)
        if special_box == 'exit':
            entry = False
            break
        special_box = [int(i) for i in special_box.split(',')]
        matrix[special_box[0], special_box[0]] = True
    print(matrix)
    matrix = np.where(matrix, 'X', ' ')
    print(matrix)
    for i in range(list[0]):
        print(' ---'*list[1])
        for j in range(list[1]):
            print('| '+matrix[i,j]+' ', end = '')
        print('|')
    print(' ---'*list[1])
print_box_modified(final_list)
