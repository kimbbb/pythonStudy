import pandas as pd

excel=pd.read_excel("조사정보1.xlsx")
df=pd.DataFrame(excel)
df.head()
a=df.loc[[1]]
excel.head()
birth=excel.loc[1]
print(birth.dtype)
print(a)







