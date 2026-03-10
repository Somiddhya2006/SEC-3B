import numpy as np 
odd=list(range(1,25,2))
O=np.array(odd)
print("Original 1D array:\n", O)
A=O.reshape(4,3)
print("\nReshaped 2D Array:\n",A)
M=A[0:2,0:2]
print("\nArray containing first two rows and first two columns:\n", M)
N=A[2:4,1:4]
print("Array containing last two rows and last two columns:\n", N)
B=np.column_stack((M,N))
print ("\nOriginal Matrix after column addition\n",B)
Column_mean=np.mean(B,axis=0)
print("\nColumn wise mean of Matrix B:",Column_mean)