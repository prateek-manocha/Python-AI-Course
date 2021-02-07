import numpy as np

A = np.random.uniform(-5,5, (9,9))
B = np.random.uniform(10,20, 9)
B = np.expand_dims(B, axis=0)
#print(A+B)
#print(A+B.T)
#print(np.all((A+B)==(A+B.T)))

def block_sum(np_arr):
    result = np.zeros((3,3))
    for k,i in enumerate(range(0,9,3)):
        for j in range(0,9,3):
            result[k, j//3] = np.sum(np_arr[i:i+3, j:j+3])
    #print(result)

A = np.arange(81).reshape(9,9)
B = np.arange(9).reshape(3,3)
#print(A)
block_sum(A)
print(B.shape)
B= np.tile(B, (3,3))
#print(B)
print(B.shape)
block_sum(B)













#end code
