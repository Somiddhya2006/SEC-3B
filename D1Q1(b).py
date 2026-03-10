import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import numpy as np 
Data= pd.read_excel('D1Q1(b).xlsx')
dff= pd.DataFrame(Data)
dff.insert(2,"x", (dff["Lower"]+dff["Upper"])/2)
dff["xf"]=dff["x"]*dff["f"]
dff["x2f"]= (dff["x"]**2)*dff["f"]
print("Dataframe:\n",dff)
sum_f= dff["f"].sum()
sum_xf=dff["xf"].sum()
sum_x2f=dff["x2f"].sum()

mean= sum_xf/sum_f
variance= (sum_x2f/sum_f)-mean**2
std= np.sqrt(variance)

print("Mean:",mean)
print("Standard Deviation", std)

plt.bar(dff["x"],dff["f"])
plt.title("No. of Students vs Mid value <x>")
plt.xlabel("Mid value <x>")
plt.ylabel("No. of Students")
plt.show()