import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('D3Q1(b).xlsx')
df=pd.DataFrame(data)
print("Original Dataframe:\n",df)

df.columns=df.columns.str.upper()
print("\n After capitalizing Column heading\n", df)

df=df.fillna('Delhi')
print("\n",df)

d=(df['YEAR']> 2015) & (df['MILEAGE']< 26)
d1=df[d]
print("\nFiltered DataFrame (YEAR > 2015 and MILEAGE < 26):\n",d1)

avg=df['MILEAGE'].mean()
print("\nAverage Mileage",avg)

grp=df.groupby('BRAND').size()
print("\nNumber of Maruti Cars",grp['Maruti'])
print("\nNumber of Hyundai Cars", grp['Huyndai'])

freq = df["BRAND"].value_counts()

plt.figure(figsize=(6,4))
freq.plot(kind='bar')
plt.xlabel("Brand")
plt.ylabel("Frequency")
plt.title("Frequency of Car Brands")
plt.show()

print("\nFrequency of each car brand:")
print(freq)
