import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('D1Q3(b).csv')
df=pd.DataFrame(data)

df.columns=["STUDENT","GENDER","PHYSICS","CHEMISTRY","MATHS","BIOLOGY"]

df["GENDER"]=df["GENDER"].str.strip().str.capitalize()
print("\n Gender Column:\n", df["GENDER"])

df=df.fillna(0)
cols=["PHYSICS","CHEMISTRY","MATHS","BIOLOGY"]
df[cols]=df[cols].astype(float)

A=df[(df["GENDER"]=="Male")&(df["MATHS"]>50)]
print("\nMale students with maths > 50\n", A)

B= df.sort_values(by="PHYSICS", ascending=False)
print("\n Marks of students in physics in descending order:\n", B)

M=df[df["GENDER"]=="Male"]["MATHS"]
F=df[df["GENDER"]=="Female"]["MATHS"]


plt.boxplot([M,F],labels=["Male","Female"])
plt.title("Comparison of Maths Marks")
plt.xlabel("Gender")
plt.ylabel("Marks")
plt.show()