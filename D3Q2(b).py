import pandas as pd
import matplotlib.pyplot as plt

# Read excel files normally
df = pd.read_excel("D3Q2(b)_1.xlsx")
df1 = pd.read_excel("D3Q2(b)_2.xlsx")

df.columns = ['Name','Age','Height']
df.index = ['r1','r2','r3','r4']

df1.columns = ['Surname','Age','Weight']
df1.index = ['r1','r2','r3','r4']

# Replace NaN values
df['Age'].fillna(30, inplace=True)
df['Height'].fillna(57, inplace=True)
df1['Age'].fillna(55, inplace=True)

print("Table I\n",df)
print("\nTable II\n",df1)

# Convert numeric columns to int
df[['Age','Height']] = df[['Age','Height']].astype(int)
df1[['Age','Weight']] = df1[['Age','Weight']].astype(int)

print("\nData Types Table I\n",df.dtypes)
print("\nData Types Table II\n",df1.dtypes)

# Merge tables on Age (right join)
merged = pd.merge(df, df1, on='Age', how='right')
print("\nMerged Table\n", merged)

# Maximum height
print("\nMax Height:", merged['Height'].max())

# Boxplot Table I
plt.boxplot(df['Age'])
plt.title("Boxplot of Age - Table I")
plt.ylabel("Age")
plt.show()

# Boundaries Table I
Q1=df['Age'].quantile(0.25)
Q3=df['Age'].quantile(0.75)
IQR=Q3-Q1
print("Lower:",Q1-1.5*IQR," Upper:",Q3+1.5*IQR)

# Boxplot Table II
plt.boxplot(df1['Age'])
plt.title("Boxplot of Age - Table II")
plt.ylabel("Age")
plt.show()

# Boundaries Table II
Q1=df1['Age'].quantile(0.25)
Q3=df1['Age'].quantile(0.75)
IQR=Q3-Q1
print("Lower:",Q1-1.5*IQR," Upper:",Q3+1.5*IQR)