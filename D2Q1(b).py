import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('D2Q1(b).xlsx')
df=pd.DataFrame(data)
print("Original data:\n",df)

df.insert(2,"X",(df["LCB "]+df["UCB"])/2)
print("\nData after adding x column\n",df)

del df["y"]
print("\nData after dropping y column\n",df)

df.insert(4,"cf",df["f"].cumsum())
print("\nData after adding cf column\n",df)

df.insert(5,"xf",(df["X"]*df["f"]))
print("\nData after adding xf column\n",df)

sum_x=df["X"].sum()
sum_f=df["f"].sum()
sum_xf=df["xf"].sum()

mean=sum_xf/sum_f
print("\n Mean of the data is:",mean)
median=df["cf"].median()
print("\n Median of the data is:",median)

plt.hist(df["X"], bins=10, weights=df["f"])
plt.title("Frequency vs Salary")
plt.ylabel("Frequency")
plt.xlabel("Salary")
plt.show()