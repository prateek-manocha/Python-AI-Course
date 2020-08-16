import numpy as np

A = np.arange(1,10).reshape(3,3)
#print(A)

def consecutive_2d_grid(num, along):
    arr = np.arange(1, (num**2+1)).reshape(num,num)
    if along == 'row':
        return arr
    elif along == 'column':
        b = np.zeros(arr.shape)
        for i in range(arr.shape[0]):
            b[:,i] = arr[i]
        return b.astype('int32')


A_f = consecutive_2d_grid(3, 'column')
print(A_f)
