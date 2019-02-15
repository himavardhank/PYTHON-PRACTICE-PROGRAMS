import pandas as pd
import matplotlib.pyplot as plt
names=['bob','jessica','mary','joun','mel']
births=[968,155,77,578,973]
dataset=list(zip(names,births))
print(dataset)
df=pd.DataFrame(data=dataset,columns=['names','births'])
print(df)
df.to_csv('births1880.csv',index=False,header=False)
df=pd.read_csv('births1880.csv')
print(df)
df=pd.read_csv('births1880.csv',header=None)
print(df)
df=pd.read_csv('births1880.csv',names=['names','births'])
print(df)
sorted=df.sort_values(['births'],ascending=True)
print(sorted)
print(sorted.head(1))
print(df['births'].max())
print(df['births'].mean())
print(df['births'].std())
pl.plot([1,2,3,4,5],list(sorted['births']))
plt.show()
