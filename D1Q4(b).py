import pandas as pd 
import matplotlib.pyplot as plt 
data= pd.read_excel('D1Q4(b).xlsx')
df=pd.DataFrame(data)
df=df.rename(columns={
    'Frequency':'F',
    'Uper_Class_Boundary':'U',
    'Lower_Class_Boundary':'L'
    
})
df['X']=(df['U']+df['L'])/2

df['CF']=df['F'].cumsum()
df['XF']=df['X']*df['F']
df['X2F']=(df['X']**2)*df['F']
print(df)

sum_f=df['F'].sum()
sum_xf=df['XF'].sum()
sum_x2f=df['X2F'].sum()

mean=sum_xf/sum_f
variance= (sum_x2f/sum_f)- mean**2
print("Mean:",mean)
print("Variance:", variance)

plt.bar(df['F'],df['X'])
plt.title("Frequency vs Midpoint")
plt.xlabel("Frequency")
plt.ylabel("Midpoint")
plt.show()