import numpy as np 
A=np.array([2.5, - 1.4, 3.8, 8.1, 0.4,-5.3, -4.7, 4.9, 11.4, 1.5, - 4.8,
-10.6])
B=A[5:11]
print (A)
print (B)
C=A.reshape(3,4)
D=B.reshape(3,2)
print(C)
print(D)

E=np.vsplit(C,3)
print(E)
F = np.array([np.mean(i) for i in E])
print("\nMean of each row (Array F):\n", F)

# Sort array A
A_sorted = np.sort(A)
print("\nSorted Array A:\n", A_sorted)