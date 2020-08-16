import numpy as np

A = np.random.randint(10, 20, (6,6))
#print(A)

def sub_array(np_arr, sb_size):
    row = np_arr.shape[0]
    col = np_arr.shape[1]
    c = []
    for i in range(0, row-1, 2):
        for j in range(0, col-1, 2):
            c.append(np.expand_dims(np_arr[i:i+sb_size, j:j+sb_size], axis = 0))
    #print(c)
    d = c[0]
    for i in range(1, len(c)):
        d = np.concatenate((d, c[i]))
    return c, d
subarray, conc = sub_array(A, 2)
import pdb
#pdb.set_trace()
B = np.random.randint(15, 20, (6,6))
#print(B)
C = np.where(A>B, A, B)
D = np.where(np.abs(A-B)%2 == 0, A, B)
print('A: ',A[0])
print('B    : ',B[0])
print('D: ',D[0])
elements = D==A
print(elements)
print(np.sum(elements))






















#end
