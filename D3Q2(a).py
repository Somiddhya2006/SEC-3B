import numpy as np

a=list(range(10,22))
A=np.array(a)
print("Array A:\n",A)

B=np.array([10,15,20])
print("\nArray B:\n",B)

C=np.setdiff1d(A,B)
print("\nArray C:\n",C)

arr=A.reshape(2,2,3)
arr=arr.astype(float)
print("\nArray after changes:\n", arr)

arr[-1,:,:]=0
arr[:,:,-1]=0
print("\nArray A after replacing 0 in last row and columns\n",arr)

i=np.where(A == 14)
print("\nIndex Number of Element 14 in array A:",i)