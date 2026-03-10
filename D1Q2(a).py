import numpy as np
even= list(range(2,25,2))
arr= np.array(even)
print("Original array:", arr)

A= arr.reshape(4,3)
print("New array of 4 x 3:\n",A)

M= A[2:4, 1:3]
print("Array containing the last two rows and last two columns:\n", M)

A_1= np.array([[1,2,3]])
A= np.vstack((A,A_1))
print("Array after adding a new row:\n", A)

A[A>10]=-1
print("Array after replacing greater values than 10 with -1:\n", A)
