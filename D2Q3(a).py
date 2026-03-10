import numpy as np 
data=list(range(200,600,20))
arr=np.array(data)
print("Array A:\n", arr)

B=arr[arr<381]
C=arr[arr>381]
print("\nArray B:\n", B)
print("\nArray C:\n", C)

D=C[::-1]
print("\nArray D\n", D)

E=D-B
print("\nArray E:\n", E)

mean=np.mean(E)
print("\nMean of Array E:\n", mean)
var=np.var(E)
print("\nVariance of Array E:\n", var)