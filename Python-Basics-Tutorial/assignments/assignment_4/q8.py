import random
import time

def generate_unique_numbers(num_unique,low,high, use_set):
    if (high-low) < num_unique:
        print('Can not generate a unique list.')
        return
    if use_set == 0:
        c = []
        start_time = time.time()
        while len(c) <= num_unique:
            x = random.randint(low, high)
            if x not in c:
                c.append(x)
        print('Time take for generating unique list: '+str(time.time()-start_time))
    #print('Initial list: ', c)

    if use_set == 1:
        c = set()
        start_time = time.time()
        while len(c) <= num_unique:
            c.add(random.randint(low, high))
    #print(c)
        print('Time take for generating set: '+str(time.time()-start_time))
generate_unique_numbers(10000, 1, 50000, 1)
