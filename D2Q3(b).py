import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('D2Q3(b).xlsx')
df=pd.DataFrame(data)
print("Original Dataframe\n",df)

df.rename(columns={
    'DIstAnce(Km)':'DISTANCE(KM)',
    'Fare':'FARE',
    'TiP':'TIPS',
    'TolLs':'TOLLS',
    'PAYmenT':'PAYMENT'
},inplace=True)
print("\nAfter renaming the columns\n", df)

df["FARE"]=df["FARE"].astype(float)
print("\nAfter changing the data type of FARE\n", df)

avg=df["TIPS"].mean()
print("\nAverage of TIPS\n", avg)

high=df["FARE"].max()
print("\nHighest FARE\n", high)

ot= df[ df["PAYMENT"]=="ONLINE"]["TIPS"].sum()
print("\nTotal TIPS for ONLINE payment\n", ot)

df.insert(4, "TOTAL", df["FARE"]+df["TIPS"]+df["TOLLS"])
print("\nAfter adding the TOTAL column\n", df)

plt.scatter(df["DISTANCE(KM)"], df["TOTAL"])
plt.title("Distance vs Trip Cost")
plt.xlabel("Distance")
plt.ylabel("Trip Cost")
plt.grid(True)
plt.show()