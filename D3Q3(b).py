import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('D3Q3(b).xlsx')
df=pd.DataFrame(data)

df.columns=df.columns.str.lower()
print(df)

T=df["population"].sum()
print("\nTotal Population", T,"billions")

df=df.fillna(0)
df['growth_rate']=df['growth_rate'].astype(float)
print("\n",df)

avg=df['growth_rate'].mean()
print("\nAverage growth rate", avg)

df["Male_Female_Ratio"]=df['male_population']/df['female_population']
print("\n",df)

df=df.sort_values(by='population', ascending=True)
print(df)

plt.bar(df['country'], df['male_population'], label='Male')
plt.bar(df['country'], df['female_population'],bottom=df['male_population'], label='Female')

plt.xlabel("Countries")
plt.ylabel("Population")
plt.title("Male vs Female Population")
plt.show()