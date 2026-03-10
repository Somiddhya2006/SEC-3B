import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('D2Q4(b).csv')
df=pd.DataFrame(data)
print("Original Dataframe:\n", df)

df.rename(columns={
    'Person':'person',
    'FOOD_PREFFERENCE':'food_preference',
    'HEIGHT ':'height',
    'WEIGHT':'weight',
    },inplace=True)
print("\nRenamed Dataframe:\n", df)

df['food_preference']=df['food_preference'].str.capitalize()
print("\nAfter capitalizing the food_preference column:\n", df)

f=df[df['food_preference']=='Nonveg']
print("Dataframe with Nonveg food preference:\n", f)

plt.bar(df['food_preference'], df['height'])
plt.title('Height by Food Preference')
plt.xlabel('Food Preference')
plt.ylabel('Height')
plt.show()