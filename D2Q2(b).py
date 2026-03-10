import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('D2Q2(b).xlsx')
df=pd.DataFrame(data)


df=df.fillna(145.0)
print (df)
print("Datatype:\n",df.dtypes)
df["Height "]=df["Height "].astype(float)
df["Gender"]=df["Gender"].str.replace('M','Male',regex=False)
df["Gender"]=df["Gender"].str.replace('F','Female', regex=False)
print(df)
d=df[df["Age"]>19]
print("\n Rows with age > 19:\n",d)
result = df.groupby("Gender")[["Height ","Age"]].agg(['mean','max','min'])

print("\nGroupBy Result:\n")
print(result)

df.boxplot(column="Height ", by="Gender")
plt.title("Height Distribution by Gender")
plt.suptitle("")
plt.xlabel("Gender")
plt.ylabel("Height")
plt.show()