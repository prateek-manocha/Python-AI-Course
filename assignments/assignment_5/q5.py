import numpy as np

A = np.linspace(-1,1,10)
print(A)
def get_prod(np_arr):
    B_basic = np.zeros((10,10))
    for i in range(10):
        for j in range(10):
            B_basic[i,j] = A[i]*A[j]
    B_eff = np.ones((10,10))
    np_arr = np.expand_dims(np_arr, axis=0)
    B_eff = (B_eff*np_arr)*np_arr.T
    B_ee = np_arr*np_arr.T
    print(B_eff)
    print(B_basic)
    print(np.all(B_eff == B_ee))
get_prod(A)
