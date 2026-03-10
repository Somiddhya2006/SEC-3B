import numpy as np
A=np.linspace(-50,50,21)
print("Array A:\n",A)

A=np.delete(A,np.where(A==0))
print("\nArray A after removing 0:\n",A)

B=A[:10]
C=A[10:]
print("\nArray B:\n",B)
print("\nArray C:\n",C)

D=np.reshape(B,(5,2))
E=np.reshape(C,(5,2))
print("\nArray D:\n",D)
print("\nArray E:\n",E)

F=np.hstack((D,E))
print("\nArray F:\n",F)
