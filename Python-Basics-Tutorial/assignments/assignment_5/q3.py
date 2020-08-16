import numpy as np

A = np.random.uniform(-5, 5, (5,7))
max_row = np.max(A, axis =1)
print(A)
print(np.mean(max_row))

max_col = np.max(A, axis = 0)
print(max_col)
print(np.min(max_col))

for j in range(A.shape[1]):
    A[:,j] = A[:,j]/np.max(A[:,j])
print(A)
A = np.random.uniform(-5, 5, (5,7))
for j in range(A.shape[0]):
    A[j] = A[j]/np.sum(A[j])

A = np.random.uniform(-5, 5, (5,7))
arg_col = np.argmax(A, axis =0)
col_args_list = []
for i in range(len(arg_col)):
    col_args_list.append([arg_col[i], i])
print(col_args_list)
#print(arg_col)
arg_row = np.argmax(A, axis =1 )
row_args_list = []
for i in range(len(arg_row)):
    row_args_list.append([i, arg_row[i]])
print(row_args_list)
for i in col_args_list:
    if i in row_args_list:
        print(i, end='  ')
        print(A[i[0], i[1]])

#print(arg_row)































#end
