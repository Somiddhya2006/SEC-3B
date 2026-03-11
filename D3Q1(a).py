import numpy as np 
arr=np.linspace(1,50,16)

A=arr.reshape(4,4)
print("Original Array A:\n",A)

B=A.astype(int)
print("\nArray B:\n",B)

print("\nShape of Array B:", B.shape)
print("\nData type of Array B:", B.dtype)

C=B[:2,:]
print("\nArray C:\n",C)
D=B[2:,:]
print("\nArray D:\n",D)

b=np.vstack((C,D))
print("\nArray b:\n",b)

comp=np.array_equal(B,b)
print("\nIs Array B equal to Array b?", comp)