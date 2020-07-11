list1 = input('Enter the input: ')
final_list = [int(i) for i in list1.split(',')]

def print_box(list):

    for i in range(list[0]):
        print(' ---'*list[1])
        print('|   '*list[1]+'|')
    print(' ---'*list[1])
print_box(final_list)
