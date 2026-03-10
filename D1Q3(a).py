import numpy as np
a=list(range(1,16,1))
arr=np.array(a)

A= arr.reshape(3,5)
print(A)

rows = np.vsplit(A,3)
print("Row wise split:")
for r in rows: 
    print (r)

B= np.hstack((A[0],A[2]))
C= np.vstack((A[0],A[2]))

print("Matrix B:\n",B)
print("Matrix C:\n",C)

s_r=A[1]
print("Mean of 2nd row:", np.mean(s_r))
print("Variance of 2nd row:", np.var(s_r))
