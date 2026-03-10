import numpy as np 
A= np.linspace(5,10,10)
print("Array A:\n",A)

B= A.reshape(2,5)
print("\n Array B:\n", B)

C= np.linspace(0,1,12)
print("\n Array C:\n",C)

D=C[-5:]
print("\nArray D:\n", D)

E=B[0,:]
print("\nArray E:\n",E)

F=np.vstack((D,E)).flatten()
print("\nArray F:\n",F)