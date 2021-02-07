import random

def random_permuted_list(list_size,low,high,num_permutations):
    c = []
    for i in range(list_size):
        c.append(random.randint(low, high))
    print('Initial list: ',c)
    for i in range(num_permutations):
        random.shuffle(c)
        print('Shuffled list: ',c)

random_permuted_list(10, 1, 5, 5)
