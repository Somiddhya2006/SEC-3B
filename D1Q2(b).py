import pandas as pd
import matplotlib.pyplot as plt 
data= pd.read_excel('D1Q2(b).xlsx',header=None)
df=pd.DataFrame(data)
print("\n",df)
df.columns=["Student Name","English","Bengali","Numerical Ability"]
df[["English","Bengali","Numerical Ability"]]=df[["English","Bengali","Numerical Ability"]].astype(float)
df=df.fillna(15)
df["Total Marks"]= df["English"]+df["Bengali"]+df["Numerical Ability"]
df=df.sort_values(by="Total Marks")
print(df)
print("The first three students along with their total marks:")
print(df[["Student Name","Total Marks"]].head(3))

plt.boxplot(df["Total Marks"])
plt.title("Boxplot of total marks")
plt.show()