import numpy as np
marks= [
    [50,55,78,72],
    [61,70,58,55],
    [48,28,60,54],
    [62,65,65,80],
    [55,49,58,73]
]
arr=np.array(marks)
print("Original Array:\n", arr)

print("Marks obtained by A,B,C\n")
print(arr[0:3])

print("Marks in Biology of D and E\n")
print(arr[3:5,2:4])

D = arr[3]
t= np.sum(D)
print("Total marks obtained by D:\n",t)

print("Maximum marks obtained by D:",np.max(D))