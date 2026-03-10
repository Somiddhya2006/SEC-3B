import numpy as np 

A= np.diag([10,20,30,40])
print("Array A:\n",A)


A[np.triu_indices(4, 1)] = 5
A[np.tril_indices(4, -1)] = 10
print("Modified Array A:\n",A)

B=np.diag([5,10,15,20])
print("\nArray B:\n",B)

greater= A > B
less=A < B
print("A > B\n", greater)
print("A < B\n", less)