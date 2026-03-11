import numpy as np 
N=50
arr=np.linspace(0,2,N)
A=np.array(arr)
print ("Array A:\n",A)
B=A*(2-A)
print ("\nArray B:\n",B)
alpha = 1e-3
C=np.zeros(N)
for i in range (2,N-2):
    C[i]=alpha*(B[i+2]+B[i-2])+(1-2*alpha)*B[i]
print ("\nArray C:\n",C)
D=C[::2]
E=C[1::2]
print ("\nArray D:\n",D)
print ("\nArray E:\n",E)

F=D.reshape(5,5)
print ("\nArray F:\n",F) 